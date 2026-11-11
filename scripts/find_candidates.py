#!/usr/bin/env python3
"""Find public work that uses LimX robots and is not in the list yet.

    python scripts/find_candidates.py                       # every robot, every source
    python scripts/find_candidates.py --robots TRON2,Oli    # only these robots
    python scripts/find_candidates.py --sources github,hf   # only these sources
    python scripts/find_candidates.py --since 2026-10-01    # only things touched since
    python scripts/find_candidates.py --mark-seen           # after review: stop reporting these

What to search for lives in scripts/sweep_config.json (robots, keywords,
sources, owners to skip). Anything already linked from README.md, or listed in
scripts/sweep_seen.txt, is left out of the report.

The script only finds candidates. A person still decides what gets listed:
a keyword hit is not proof that a project really uses the robot.

Needs only the Python standard library. GitHub code search needs a token in
GITHUB_TOKEN or GH_TOKEN (any token works, no scopes needed); without one the
script falls back to repository search, which finds much less.
"""
import argparse
import datetime
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
UA = "awesome-limx-sweep (+https://github.com/limxdynamics/awesome-limx)"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def get(url, headers=None, retries=3, accept_json=True):
    """GET a URL, return parsed JSON (or text). None when it keeps failing."""
    h = {"User-Agent": UA}
    h.update(headers or {})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=40) as r:
                body = r.read().decode("utf-8", "replace")
                return json.loads(body) if accept_json else body
        except urllib.error.HTTPError as e:
            limited = e.code == 429 or e.headers.get("Retry-After") or e.headers.get("x-ratelimit-remaining") == "0"
            if limited and attempt < retries - 1:
                wait = int(e.headers.get("Retry-After") or 0) or 30 * (attempt + 1)
                log(f"    rate limited ({e.code}), waiting {wait}s")
                time.sleep(min(wait, 120))
                continue
            log(f"    HTTP {e.code} for {url[:110]}")
            return None
        except Exception as e:  # network hiccup, bad JSON
            if attempt < retries - 1:
                time.sleep(5)
                continue
            log(f"    failed: {e} for {url[:110]}")
            return None


def gh(path, retries=3):
    h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if TOKEN:
        h["Authorization"] = "Bearer " + TOKEN
    return get("https://api.github.com" + path, h, retries)


# ---------------------------------------------------------------- what we already have

def load_known():
    """Everything already linked from README.md, plus the reviewed list."""
    text = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
    known = {"github": set(), "arxiv": set(), "doi": set(), "hf": set(), "hf_owner": set()}
    for m in re.finditer(r"github\.com/([\w.-]+)/([\w.-]+)", text):
        known["github"].add((m.group(1) + "/" + m.group(2)).lower().removesuffix(".git"))
    for m in re.finditer(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", text):
        known["arxiv"].add(m.group(1))
    for m in re.finditer(r"doi\.org/(10\.[^\s)|]+)", text):
        known["doi"].add(m.group(1).lower())
    for m in re.finditer(r"huggingface\.co/(?:(datasets|spaces)/)?([\w.-]+)(?:/([\w.-]+))?", text):
        owner, name = m.group(2), m.group(3)
        if owner in ("models", "datasets", "spaces"):  # search-style link: ?author=xxx
            a = re.search(r"author=([\w.-]+)", text[m.start():m.start() + 200])
            if a:
                known["hf_owner"].add(a.group(1).lower())
        elif name:
            known["hf"].add((owner + "/" + name).lower())
        else:
            known["hf_owner"].add(owner.lower())
    seen = set()
    p = os.path.join(HERE, "sweep_seen.txt")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            line = line.split("#")[0].strip()
            if line:
                seen.add(line.lower())
    return known, seen


# ---------------------------------------------------------------- sources

def robots_for(text, cfg, wanted):
    """Which configured robots a piece of text mentions."""
    out = []
    low = text.lower()
    for name in wanted:
        r = cfg["robots"][name]
        if any(k.lower() in low for k in r.get("code", []) + r.get("text", [])):
            out.append(name)
    return out


def src_github(cfg, wanted, known, seen, since):
    """Code search per keyword, then one call per new repo for stars and dates."""
    s = cfg["sources"]["github"]
    queries = []  # (keyword, robot or None)
    for name in wanted:
        queries += [(k, name) for k in cfg["robots"][name].get("code", [])]
    queries += [(k, None) for k in cfg.get("company", {}).get("code", [])]
    skip_owner = {o.lower() for o in cfg.get("skip_owners", [])}
    hits = {}  # repo -> {robots, keywords, paths}
    noise = re.compile(s.get("ignore_paths") or r"$^")
    for kw, robot in queries:
        log(f"  github: {kw}")
        for page in range(1, s.get("pages", 3) + 1):
            if TOKEN:
                q = urllib.parse.quote(kw)
                d = gh(f"/search/code?q={q}&per_page=100&page={page}")
                time.sleep(7)  # code search allows 10 requests a minute
            else:
                q = urllib.parse.quote(kw + " in:name,description,readme")
                d = gh(f"/search/repositories?q={q}&per_page=100&page={page}&sort=updated")
                time.sleep(7)
            items = (d or {}).get("items") or []
            for it in items:
                repo = it.get("repository", it)
                full = repo["full_name"]
                low = full.lower()
                if low in known["github"] or "gh:" + low in seen or low in seen:
                    continue
                if repo["owner"]["login"].lower() in skip_owner or repo.get("fork"):
                    continue
                h = hits.setdefault(full, {"robots": set(), "kw": set(), "paths": [], "solid": not TOKEN})
                # A hit in a news dump or a dated post says the robot was mentioned, not used.
                if it.get("path") and not noise.search(it["path"]):
                    h["solid"] = True
                if robot:
                    h["robots"].add(robot)
                h["kw"].add(kw)
                if it.get("path") and len(h["paths"]) < 3:
                    h["paths"].append(it["path"])
            if len(items) < 100:
                break
    out = []
    dropped = [f for f, h in hits.items() if not h["solid"]]
    hits = {f: h for f, h in hits.items() if h["solid"]}
    if dropped:
        log(f"  github: left out {len(dropped)} repos that only mention the keywords in news or data files")
    limit = s.get("max_repos", 400)
    log(f"  github: {len(hits)} new repos, fetching details" + (f" for the first {limit}" if len(hits) > limit else ""))
    for full, h in list(hits.items())[:limit]:
        d = gh("/repos/" + full, retries=2) or {}
        time.sleep(0.5)
        if d.get("fork"):
            continue
        pushed = (d.get("pushed_at") or "")[:10]
        if since and pushed and pushed < since:
            continue
        if d.get("stargazers_count", 0) < s.get("min_stars", 0):
            continue
        out.append({
            "key": "gh:" + full.lower(), "title": full, "url": "https://github.com/" + full,
            "robots": sorted(h["robots"]), "date": pushed, "stars": d.get("stargazers_count", 0),
            "note": (d.get("description") or "").strip()[:140],
            "why": ", ".join(sorted(h["kw"])) + (" in " + ", ".join(h["paths"]) if h["paths"] else ""),
        })
    out.sort(key=lambda c: (-c["stars"], c["title"]))
    return out


def text_keywords(cfg, wanted):
    kws = list(cfg.get("company", {}).get("text", []))
    for name in wanted:
        kws += cfg["robots"][name].get("text", [])
    return list(dict.fromkeys(kws))


def src_arxiv(cfg, wanted, known, seen, since):
    """arXiv searches titles and abstracts only, so this finds papers that name the robot up front."""
    out, done = [], set()
    ns = {"a": "http://www.w3.org/2005/Atom"}
    for kw in text_keywords(cfg, wanted):
        log(f"  arxiv: {kw}")
        q = urllib.parse.quote(f'all:"{kw}"')
        body = get(f"http://export.arxiv.org/api/query?search_query={q}&sortBy=submittedDate&sortOrder=descending"
                   f"&max_results={cfg['sources']['arxiv'].get('max_results', 50)}", accept_json=False)
        time.sleep(3)
        if not body:
            continue
        try:
            feed = ET.fromstring(body)
        except ET.ParseError:
            continue
        for e in feed.findall("a:entry", ns):
            aid = re.sub(r"v\d+$", "", e.findtext("a:id", "", ns).rsplit("/", 1)[-1])
            date = e.findtext("a:published", "", ns)[:10]
            if aid in known["arxiv"] or "arxiv:" + aid in seen or aid in done or (since and date < since):
                continue
            done.add(aid)
            title = " ".join(e.findtext("a:title", "", ns).split())
            summary = e.findtext("a:summary", "", ns)
            out.append({"key": "arxiv:" + aid, "title": title, "url": "https://arxiv.org/abs/" + aid,
                        "robots": robots_for(title + " " + summary, cfg, wanted), "date": date,
                        "stars": None, "note": "", "why": kw})
    return out


def src_openalex(cfg, wanted, known, seen, since):
    """OpenAlex searches full text, so it also finds papers that only name the robot in the experiments."""
    out, done = [], set()
    s = cfg["sources"]["openalex"]
    start = since or (datetime.date.today() - datetime.timedelta(days=s.get("default_days", 365))).isoformat()
    mail = s.get("mailto", "")
    for kw in text_keywords(cfg, wanted):
        log(f"  openalex: {kw}")
        f = urllib.parse.quote(f'fulltext.search:"{kw}",from_publication_date:{start}')
        d = get(f"https://api.openalex.org/works?filter={f}&per-page={s.get('max_results', 50)}"
                f"&sort=publication_date:desc&select=id,doi,title,publication_date,ids,primary_location"
                + (f"&mailto={mail}" if mail else ""))
        time.sleep(1)
        for w in (d or {}).get("results") or []:
            doi = (w.get("doi") or "").replace("https://doi.org/", "").lower()
            m = re.search(r"arxiv\.(\d{4}\.\d{4,5})", doi)
            aid = m.group(1) if m else ""
            key = "arxiv:" + aid if aid else ("doi:" + doi if doi else "openalex:" + w["id"].rsplit("/", 1)[-1])
            if key in done or key.lower() in seen or (aid and aid in known["arxiv"]) or (doi and doi in known["doi"]):
                continue
            done.add(key)
            url = ("https://arxiv.org/abs/" + aid) if aid else (w.get("doi") or w["id"])
            title = " ".join((w.get("title") or "").split())
            out.append({"key": key, "title": title, "url": url, "robots": robots_for(title, cfg, wanted),
                        "date": w.get("publication_date") or "", "stars": None, "note": "", "why": kw})
    return out


def src_hf(cfg, wanted, known, seen, since):
    """Hugging Face matches repo names only, so keywords here are short name fragments."""
    out, done = [], set()
    kws = list(cfg.get("company", {}).get("hf", []))
    for name in wanted:
        kws += [(k, name) for k in cfg["robots"][name].get("hf", [])]
    skip_owner = {o.lower() for o in cfg.get("skip_owners", [])}
    for kw in kws:
        kw, robot = kw if isinstance(kw, tuple) else (kw, None)
        log(f"  hf: {kw}")
        for kind in ("models", "datasets", "spaces"):
            d = get(f"https://huggingface.co/api/{kind}?search={urllib.parse.quote(kw)}&limit=100&sort=lastModified&direction=-1")
            time.sleep(1)
            for it in d or []:
                rid = it.get("id") or ""
                owner = rid.split("/")[0].lower()
                key = "hf:" + rid.lower()
                date = (it.get("lastModified") or it.get("createdAt") or "")[:10]
                if (rid.lower() in known["hf"] or owner in known["hf_owner"] or owner in skip_owner
                        or key in seen or key in done or (since and date and date < since)):
                    continue
                done.add(key)
                prefix = "" if kind == "models" else kind + "/"
                out.append({"key": key, "title": f"{rid} ({kind[:-1]})", "url": f"https://huggingface.co/{prefix}{rid}",
                            "robots": [robot] if robot else [], "date": date, "stars": it.get("downloads"),
                            "note": "", "why": kw})
    return out


SOURCES = {"github": ("GitHub", src_github, "stars"), "hf": ("Hugging Face", src_hf, "downloads"),
           "arxiv": ("arXiv (title and abstract)", src_arxiv, None), "openalex": ("OpenAlex (full text)", src_openalex, None)}


# ---------------------------------------------------------------- report

def report(results, wanted, since):
    total = sum(len(v) for v in results.values())
    lines = [f"# Candidate sweep, {datetime.date.today().isoformat()}", "",
             f"{total} candidates not yet in the list. Robots: {', '.join(wanted)}."
             + (f" Only items touched since {since}." if since else ""), "",
             "A keyword hit is not proof. Open each one and check that it really uses the robot before listing it.",
             "When you are done, run `python scripts/find_candidates.py --mark-seen` so the rejected ones stop showing up.", ""]
    for key, items in results.items():
        label, _, metric = SOURCES[key]
        lines += [f"## {label}: {len(items)}", ""]
        if not items:
            lines += ["Nothing new.", ""]
            continue
        head = "| Candidate | Robot | " + (metric.capitalize() + " | " if metric else "") + "Date | Matched |"
        lines += [head, "|" + "---|" * (head.count("|") - 1)]
        for c in items:
            note = (" — " + c["note"].replace("|", "/")) if c["note"] else ""
            row = f"| [{c['title'].replace('|', '/')}]({c['url']}){note} | {' '.join(c['robots']) or '?'} | "
            if metric:
                row += f"{c['stars'] if c['stars'] is not None else ''} | "
            row += f"{c['date']} | {c['why'].replace('|', '/')[:120]} |"
            lines.append(row)
        lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--config", default=os.path.join(HERE, "sweep_config.json"))
    ap.add_argument("--robots", help="comma-separated robot names from the config (default: all)")
    ap.add_argument("--sources", help="comma-separated: " + ",".join(SOURCES) + " (default: those enabled in the config)")
    ap.add_argument("--since", help="YYYY-MM-DD, or a number of days back")
    ap.add_argument("--out", default="sweep_report.md", help="where to write the report")
    ap.add_argument("--mark-seen", action="store_true",
                    help="add the candidates from the last run (sweep_candidates.json) to sweep_seen.txt")
    a = ap.parse_args()

    state = os.path.join(ROOT, "sweep_candidates.json")
    if a.mark_seen:
        if not os.path.exists(state):
            sys.exit("no sweep_candidates.json: run a sweep first")
        _, seen = load_known()
        new = [k for k in json.load(open(state, encoding="utf-8")) if k.lower() not in seen]
        with open(os.path.join(HERE, "sweep_seen.txt"), "a", encoding="utf-8") as f:
            f.write(f"\n# reviewed {datetime.date.today().isoformat()}\n" + "".join(k + "\n" for k in new))
        print(f"marked {len(new)} candidates as reviewed")
        return

    cfg = json.load(open(a.config, encoding="utf-8"))
    wanted = [r.strip() for r in a.robots.split(",")] if a.robots else list(cfg["robots"])
    bad = [r for r in wanted if r not in cfg["robots"]]
    if bad:
        sys.exit(f"not in the config: {', '.join(bad)}. Known robots: {', '.join(cfg['robots'])}")
    sources = [s.strip() for s in a.sources.split(",")] if a.sources else \
        [s for s in SOURCES if cfg["sources"].get(s, {}).get("enabled", True)]
    since = a.since
    if since and since.isdigit():
        since = (datetime.date.today() - datetime.timedelta(days=int(since))).isoformat()
    if "github" in sources and not TOKEN:
        log("no GITHUB_TOKEN: using repository search only, expect far fewer GitHub hits")

    known, seen = load_known()
    results = {}
    for s in sources:
        if s not in SOURCES:
            sys.exit(f"unknown source {s}. Choose from: {', '.join(SOURCES)}")
        log(f"{SOURCES[s][0]}")
        try:
            results[s] = SOURCES[s][1](cfg, wanted, known, seen, since)
        except Exception as e:  # one source down should not lose the others
            log(f"  {s} failed: {e}")
            results[s] = []
    text = report(results, wanted, since)
    open(a.out, "w", encoding="utf-8").write(text + "\n")
    json.dump([c["key"] for v in results.values() for c in v], open(state, "w", encoding="utf-8"), indent=0)
    print(f"{sum(len(v) for v in results.values())} candidates -> {a.out}")


if __name__ == "__main__":
    main()
