#!/usr/bin/env python3
"""Build the browsable gallery (docs/index.html) from the README tables.

    python scripts/build_gallery.py          # write docs/index.html
    python scripts/build_gallery.py --check  # exit 1 if it is out of date
    python scripts/build_gallery.py --strict # exit 1 on a problem in gallery.json, write nothing

The README files are the source, as for the robot pages. Media and the
featured picks live in scripts/gallery.json:

    {
      "featured": ["faststair", "where-to-learn"],        # anchor ids, shown first
      "media": {
        "ame-2": {"video": "https://youtu.be/...",          # YouTube or bilibili link
                  "thumb": "thumbs/ame-2.webp"}             # file under docs/
      }
    }

A thumbnail is picked in this order: "thumb" in gallery.json, a file
docs/thumbs/<id>.(webp|jpg|png|gif), the first YouTube link of the entry,
a frame of a video file, then an illustration drawn in the page from the
robot and the description (scripts/gallery_illustrations.js), labelled as such.
"video" can be a YouTube or bilibili link, or an https .mp4/.webm file on the
project's own site. Do not edit docs/index.html by
hand: change the README or gallery.json and run this script.
"""
import argparse
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
OUT = os.path.join(DOCS, "index.html")
TEMPLATE = os.path.join(ROOT, "scripts", "gallery_template.html")
ILLUSTRATIONS = os.path.join(ROOT, "scripts", "gallery_illustrations.js")
CONFIG = os.path.join(ROOT, "scripts", "gallery.json")

ROBOTS = ["TRON1", "TRON2", "Oli", "Luna", "P1", "W1"]
EDITIONS = [("en", "README.md"), ("cn", "README_cn.md"), ("ja", "README_ja.md"), ("ko", "README_ko.md")]
# Type labels in each edition, mapped to one key.
TYPES = {
    "Code": "code", "代码": "code", "コード": "code", "코드": "code",
    "Tutorial": "tutorial", "教程": "tutorial", "チュートリアル": "tutorial", "튜토리얼": "tutorial",
    "Paper": "paper", "论文": "paper", "論文": "paper", "논문": "paper",
    "News": "news", "报道": "news", "報道": "news", "보도": "news",
}
CODE_HOSTS = ("github.com", "gitlab.com", "gitee.com", "bitbucket.org", "huggingface.co")
ROW_ID = re.compile(r'<a id="p-([^"]+)"></a>')
LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")


def cells(row):
    # Cells are separated by " | "; a literal pipe inside a cell would be escaped.
    return [c.strip() for c in re.split(r"(?<!\\)\|", row.strip()[1:-1])]


def inline(md):
    """The small subset of Markdown that appears in a cell, as HTML."""
    out, pos = [], 0
    for m in LINK.finditer(md):
        out.append(_text(md[pos:m.start()]))
        out.append('<a href="%s" rel="noopener" target="_blank">%s</a>' % (html.escape(m.group(2), True), _text(m.group(1))))
        pos = m.end()
    out.append(_text(md[pos:]))
    return "".join(out).strip()


def _text(s):
    s = html.escape(s.replace("&nbsp;", " "), False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*([^*]+)\*(?![\w*])", r"<i>\1</i>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def plain(md):
    return re.sub(r"<[^>]+>", "", html.unescape(inline(md)))


def video_of(url):
    """(provider, id) for a YouTube or bilibili link or a video file, else None."""
    m = re.search(r"(?:youtu\.be/|youtube\.com/(?:watch\?(?:.*&)?v=|shorts/|embed/))([\w-]{11})", url)
    if m:
        return "youtube", m.group(1)
    m = re.search(r"bilibili\.com/video/(BV\w+)", url)
    if m:
        return "bilibili", m.group(1)
    if re.match(r"https://", url) and re.search(r"\.(mp4|webm)(?:[?#]|$)", url, re.I):
        return "file", url  # a video file on the project's own site, played in place
    return None


def parse(path):
    """Entries of one README edition: {id: dict}, plus the section names in order."""
    text = open(path, encoding="utf-8").read()
    entries, sections = {}, []
    sec = sub = None
    header = None
    for ln in text.split("\n"):
        m = re.match(r"^(#{2,3}) (.*)$", ln)
        if m:
            if len(m.group(1)) == 2:
                sec, sub = m.group(2).strip(), None
            else:
                sub = m.group(2).strip()
            header = None
            continue
        if ln.startswith("|") and header is None and "a id=" not in ln:
            header = cells(ln)
            continue
        m = ROW_ID.search(ln)
        if not m or not ln.startswith("|"):
            continue
        if sec not in sections:
            sections.append(sec)
        c = cells(ln)
        has_type = len(c) >= 6
        project, robot, author, year = c[0], c[1], c[2], c[3]
        type_label = c[4] if has_type else ""
        links_md = c[-1]
        nm = re.search(r"\*\*(.+?)\*\*\s*[:：]?\s*(.*)$", ROW_ID.sub("", project))
        name, desc = (nm.group(1), nm.group(2)) if nm else (plain(project), "")
        links = [{"label": lab, "url": url} for lab, url in LINK.findall(links_md)]
        entries[m.group(1)] = {
            "name": plain(name),
            "desc": inline(desc),
            "robots": [r for r in re.findall(r"`([^`]+)`", robot)],
            "sim": bool(re.search(r"\*[^*`]+\*", robot)),
            "simLabel": (re.search(r"\*([^*`]+)\*", robot) or [None, ""])[1],
            "author": inline(author),
            "year": int(year) if year.isdigit() else 0,
            "type": TYPES.get(type_label.strip()),
            "typeLabel": type_label.strip(),
            "links": links,
            "section": sections.index(sec),
            "sub": sub or "",
        }
    return entries, sections


def build():
    cfg = json.load(open(CONFIG, encoding="utf-8")) if os.path.exists(CONFIG) else {}
    editions = {lang: parse(os.path.join(ROOT, f)) for lang, f in EDITIONS}
    base, _ = editions["en"]
    problems = []

    items = []
    for eid, e in base.items():
        item = {
            "id": eid, "robots": e["robots"], "sim": e["sim"], "year": e["year"],
            "section": e["section"], "urls": [l["url"] for l in e["links"]],
            "t": {},
        }
        typ = e["type"]
        if typ is None:  # sections without a Type column (tools): code if any link is a code host
            typ = "code" if any(h in u for u in item["urls"] for h in CODE_HOSTS) else "paper"
        item["type"] = typ
        for lang, (ents, _) in editions.items():
            x = ents.get(eid)
            if x is None:
                problems.append("%s: entry %s missing from %s" % (lang, eid, lang))
                x = e
            item["t"][lang] = {
                "name": x["name"], "desc": x["desc"], "author": x["author"], "sub": x["sub"],
                "sim": x["simLabel"], "type": x["typeLabel"],
                "links": [l["label"] for l in x["links"]],
            }
        # Media: config first, then a file in docs/thumbs, then the entry's own video.
        media = dict(cfg.get("media", {}).get(eid, {}))
        if "thumb" not in media:
            for ext in ("webp", "jpg", "png", "gif"):
                if os.path.exists(os.path.join(DOCS, "thumbs", "%s.%s" % (eid, ext))):
                    media["thumb"] = "thumbs/%s.%s" % (eid, ext)
                    break
        if "video" not in media:
            media["video"] = next((u for u in item["urls"] if video_of(u)), None)
        v = video_of(media["video"]) if media.get("video") else None
        if v:
            item["video"] = {"provider": v[0], "id": v[1], "url": media["video"]}
            if "thumb" not in media and v[0] == "youtube":
                media["thumb"] = "https://i.ytimg.com/vi/%s/hqdefault.jpg" % v[1]
        elif media.get("video"):
            problems.append("gallery.json: %s video is not a YouTube, bilibili or https .mp4/.webm link" % eid)
        if media.get("thumb"):
            if not media["thumb"].startswith("http") and not os.path.exists(os.path.join(DOCS, media["thumb"])):
                problems.append("gallery.json: %s thumb %s not found under docs/" % (eid, media["thumb"]))
            item["thumb"] = media["thumb"]
        items.append(item)

    ids = {i["id"] for i in items}
    for eid in list(cfg.get("featured", [])) + list(cfg.get("media", {})):
        if eid not in ids:
            problems.append("gallery.json: %s is not an entry in the README" % eid)

    data = {
        "robots": ROBOTS,
        "sections": {lang: secs for lang, (_, secs) in editions.items()},
        "featured": [f for f in cfg.get("featured", []) if f in ids],
        "items": items,
    }
    blob = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    blob = blob.replace("</", "<\\/")  # keep it inert inside <script>
    page = open(TEMPLATE, encoding="utf-8").read()
    page = page.replace("/*GALLERY_DATA*/{}", blob)
    page = page.replace("/*GALLERY_ILLUSTRATIONS*/", open(ILLUSTRATIONS, encoding="utf-8").read().replace("</", "<\\/"))
    page = "<!-- Generated by scripts/build_gallery.py from the README. Do not edit by hand. -->\n" + page
    return page, problems


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="exit 1 if docs/index.html is out of date")
    ap.add_argument("--strict", action="store_true", help="exit 1 on any problem, write nothing (for pull requests)")
    a = ap.parse_args()
    page, problems = build()
    for p in problems:
        print("WARN ", p)
    if a.strict:
        if problems:
            sys.exit(1)
        print("OK  gallery builds without problems")
        return
    current = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
    if a.check:
        if current != page:
            print("docs/index.html is out of date: run python scripts/build_gallery.py")
            sys.exit(1)
        print("OK  gallery is up to date")
        return
    os.makedirs(DOCS, exist_ok=True)
    nojekyll = os.path.join(DOCS, ".nojekyll")
    if not os.path.exists(nojekyll):
        open(nojekyll, "w").close()
    if current != page:
        with open(OUT, "w", encoding="utf-8", newline="\n") as f:
            f.write(page)
        print("wrote docs/index.html")
    else:
        print("docs/index.html already up to date")


if __name__ == "__main__":
    main()
