#!/usr/bin/env python3
"""Validate the awesome-limx list.

Two levels, on purpose, because the layout of this file will keep changing:

  ERROR  the page is broken or content is missing. Fails the build.
         - duplicate anchors, or a #p-... link that resolves to nothing
         - a blank line inside a table, which ends it: every row below renders
           as plain text instead of a table row
         - a table row with a different number of cells than its header
         - an entry present in one language edition but not the other

  WARN   worth a look, but a change of layout must not fail the build.
         - a printed count that no longer matches the table under it
         - a Type label that disagrees with the links in the same row
         - a total in the header that disagrees with the entries found

Anything the script cannot recognise is skipped silently, not reported: if the
count line or the By-robot summary is rewritten in a new shape, the check simply
stops applying until it is taught the new shape.

Standard library only, so CI needs no install step.
"""

import argparse
import os
import re
import sys
import urllib.error
import urllib.request

EDITIONS = [("README.md", "en"), ("README_cn.md", "cn"), ("README_ja.md", "ja"), ("README_ko.md", "ko")]

ANCHOR = re.compile(r'<a id="p-([^"]+)"></a>')
LINK_REF = re.compile(r"\]\(#p-([^)]+)\)")
TABLE_SEP = re.compile(r"^\|[\s\-:|]+\|$")
HEADING = re.compile(r"^(#{2,3})\s+(.*)$")
ROBOT_ROW = re.compile(r"^-\s*\*\*([^*]+)\*\*\s*[:：]\s*(.*)$")

TYPE_CODE = {"en": "Code", "cn": "代码", "ja": "コード", "ko": "코드"}
TYPE_PAPER = {"en": "Paper", "cn": "论文", "ja": "論文", "ko": "논문"}
TYPE_TUTORIAL = {"en": "Tutorial", "cn": "教程", "ja": "チュートリアル", "ko": "튜토리얼"}
TYPE_NEWS = {"en": "News", "cn": "报道", "ja": "報道", "ko": "보도"}
# Link kinds that only report on something: a media report, a result announcement, a video.
NEWS_KINDS = {"news", "报道", "報道", "보도", "result", "成绩", "結果", "결과", "video", "视频", "動画", "영상"}

CODE_HOSTS = ("github.com", "gitlab.com", "bitbucket.org")
LINK_MARK = re.compile(r"\[?\[(\w+)\]\((https?://[^)]+)\)")

MAX_SHOWN = 12


class Report:
    def __init__(self):
        self.items = []

    def error(self, kind, msg):
        self.items.append(("ERROR", kind, msg))

    def warn(self, kind, msg):
        self.items.append(("WARN", kind, msg))

    def dump(self, strict):
        errors = [i for i in self.items if i[0] == "ERROR"]
        warns = [i for i in self.items if i[0] == "WARN"]

        for title, group in (("error", errors), ("warning", warns)):
            if not group:
                continue
            print("%d %s(s):\n" % (len(group), title))
            for n, (_, kind, msg) in enumerate(group[:MAX_SHOWN], 1):
                print("  %2d. [%s] %s" % (n, kind, msg))
            if len(group) > MAX_SHOWN:
                print("  ... and %d more" % (len(group) - MAX_SHOWN))
            print()

        if errors:
            print("FAIL  %d error(s), %d warning(s)" % (len(errors), len(warns)))
            return 1
        if warns and strict:
            print("FAIL  --strict: %d warning(s)" % len(warns))
            return 1
        if warns:
            print("PASS  with %d warning(s)" % len(warns))
        else:
            print("OK  no problems found")
        return 0


def split_row(line):
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|"):
        body = body[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", body)]


def headings(text):
    """Yield (line, level, section, subsection) for every line."""
    section = sub = None
    for line in text.splitlines():
        h = HEADING.match(line)
        if h:
            if h.group(1) == "##":
                section, sub = h.group(2).strip(), None
            else:
                sub = h.group(2).strip()
            yield line, len(h.group(1)), section, sub
        else:
            yield line, 0, section, sub


def tables(text):
    """Yield each markdown table with the heading it sits under.

    Strict on purpose: a blank line ends a table. GitHub renders a pipe row
    after a blank line as ordinary text, so a lenient parser here would report
    a healthy table for a page that visibly is not one. check_table_breaks
    reports the blank lines themselves.
    """
    cur = None
    for line, level, section, sub in headings(text):
        if level:
            if cur is not None:
                yield cur
                cur = None
            continue

        s = line.strip()
        if s.startswith("|"):
            if cur is None:
                cur = {"section": section, "sub": sub, "header": split_row(line),
                       "rows": [], "sep_seen": False}
            elif TABLE_SEP.match(s):
                if cur["sep_seen"]:
                    yield cur
                    cur = {"section": section, "sub": sub, "header": split_row(line),
                           "rows": [], "sep_seen": False}
                cur["sep_seen"] = True
            else:
                cur["rows"].append(split_row(line))
        elif cur is not None:
            yield cur
            cur = None

    if cur is not None:
        yield cur


def check_table_breaks(text, path, report):
    """Report blank lines that cut a table in two.

    GitHub ends a table at the first blank line. Everything after it is text.
    The failure is invisible in a lenient parser and obvious on the page, so it
    is checked before anything is parsed out of the tables.
    """
    lines = text.split("\n")
    broken = False
    i = 0
    while i < len(lines):
        if not lines[i].strip().startswith("|"):
            i += 1
            continue
        start = i
        blanks = 0
        j = i
        while j < len(lines):
            s = lines[j].strip()
            if s.startswith("|"):
                if blanks:
                    report.error(
                        "table",
                        "%s:%d: a blank line ends the table, so this row renders as text "
                        "(table starts at line %d)" % (path, j + 1, start + 1))
                    broken = True
                    blanks = 0
                j += 1
            elif not s:
                blanks += 1
                j += 1
            else:
                break
        i = j
    return broken


def is_entry_table(t):
    return len(t["header"]) >= 4 and t["header"][0].strip().lower() in ("project", "项目", "プロジェクト", "프로젝트")


def type_index(t):
    for i, h in enumerate(t["header"]):
        if h.strip().lower() == "type" or h.strip() in ("类型", "種別", "유형"):
            return i
    return None


def urls_in(text):
    return re.findall(r"\]\((https?://[^)]+)\)", text)


def link_items(cell):
    """The [[kind](url)] pairs in a Links cell."""
    return [(m.group(1), m.group(2)) for m in LINK_MARK.finditer(cell)]


def is_runnable(items):
    """Something to clone or download.

    A Hugging Face account page counts: it lists that account's models and
    datasets, so a reader who lands there can still download something. A
    GitHub profile does not - it may hold nothing related to the entry.
    """
    for _, url in items:
        if "huggingface.co/spaces" in url:
            continue
        if "huggingface.co/" in url or "modelscope.cn/" in url:
            return True
        if any(h in url for h in CODE_HOSTS) and url.rstrip("/").count("/") >= 4:
            return True
    return False


def is_walkable(items):
    """Something to follow along with: a tutorial or a Space."""
    return any(kind in ("tutorial", "教程", "チュートリアル", "튜토리얼") or "huggingface.co/spaces" in url for kind, url in items)


def check_type(label_type, items, lang, path, table, report):
    """The four values answer one question: what can a reader do with this?

    Code      clone or download it
    Tutorial  follow it, but there is no package to take away
    Paper     read it (paper, project page, write-up)
    News      only a media report, an announcement or a result
    """
    runnable = is_runnable(items)
    walkable = is_walkable(items)
    news_only = bool(items) and all(kind in NEWS_KINDS for kind, _ in items)

    if label_type in TYPE_CODE.values():
        if not runnable:
            report.warn("type", "%s / %r: marked %s but links nothing to clone or download"
                        % (path, table, label_type))
    elif label_type in TYPE_TUTORIAL.values():
        if not walkable:
            report.warn("type", "%s / %r: marked %s but links no tutorial or Space"
                        % (path, table, label_type))
        elif runnable:
            report.warn("type", "%s / %r: marked %s but also links code or a model"
                        % (path, table, label_type))
    elif label_type in TYPE_PAPER.values():
        if runnable or walkable:
            report.warn("type", "%s / %r: marked %s but links something to run"
                        % (path, table, label_type))
        elif news_only:
            report.warn("type", "%s / %r: marked %s but links only reports: use %s"
                        % (path, table, label_type, TYPE_NEWS[lang]))
    elif label_type in TYPE_NEWS.values():
        if runnable or walkable or not news_only:
            report.warn("type", "%s / %r: marked %s but links more than reports"
                        % (path, table, label_type))
    else:
        report.warn("type", "%s / %r: unrecognised type %r, expected %s / %s / %s / %s"
                    % (path, table, label_type, TYPE_CODE[lang], TYPE_TUTORIAL[lang],
                       TYPE_PAPER[lang], TYPE_NEWS[lang]))


def table_label(t):
    return t["section"] if not t["sub"] else "%s / %s" % (t["section"], t["sub"])


def check_tables(text, lang, path, report):
    """Column counts, anchors per entry, and the Type column."""
    entries = {}
    row_counts = {}

    for t in tables(text):
        ncol = len(t["header"])
        label = table_label(t)

        if not is_entry_table(t):
            for cells in t["rows"]:
                if len(cells) != ncol:
                    report.error("columns", "%s / %r: a row has %d cells, the header has %d"
                                 % (path, t["section"], len(cells), ncol))
            continue

        tidx = type_index(t)
        for cells in t["rows"]:
            if len(cells) != ncol:
                report.error("columns", "%s / %r: a row has %d cells, the header has %d: %r"
                             % (path, label, len(cells), ncol, cells[0][:45]))
                continue

            m = ANCHOR.search(cells[0])
            if m:
                aid = m.group(1)
                if aid in entries:
                    report.error("anchors", "%s: anchor p-%s is used by two entries" % (path, aid))
                entries.setdefault(aid, label)
            else:
                report.warn("anchors", "%s / %r: entry has no <a id=\"p-...\"> anchor: %r"
                            % (path, label, cells[0][:50]))

            if tidx is None:
                continue
            check_type(cells[tidx].strip(), link_items(cells[-1]), lang, path, label, report)

        row_counts[t["section"]] = row_counts.get(t["section"], 0) + len(t["rows"])

    return entries, row_counts


def check_refs(text, path, entries, report):
    for ref in sorted(set(LINK_REF.findall(text))):
        if ref not in entries:
            report.error("links", "%s: link #p-%s points at no entry" % (path, ref))


def check_counts(text, path, row_counts, report):
    """Printed counts, only when a line still looks like a count line."""
    section = None
    for line, level, sec, sub in headings(text):
        if level == 2:
            section = sec
        s = line.strip()
        if not (s.startswith("_") and s.endswith("_")):
            continue
        m = re.match(r"^_(\d+)(?!\d)", s)
        if not m:
            continue
        declared = int(m.group(1))
        actual = row_counts.get(section)
        if actual is None:
            report.warn("counts", "%s: count line under %r has no table" % (path, section))
        elif actual != declared:
            report.warn("counts", "%s: %r says %d, the tables hold %d"
                        % (path, section, declared, actual))

    for m in re.finditer(r"\*\*(\d+)\*\*\s*(?:projects|个项目|プロジェクト|개 프로젝트)", text):
        total = len(ANCHOR.findall(text))
        if int(m.group(1)) != total:
            report.warn("counts", "%s: header says %s entries, found %d"
                        % (path, m.group(1), total))


def check_by_robot(text, path, report):
    """The By-robot table should agree with the Robot column. Warn only.

    Reads rows shaped like  | `TRON1` | **52** | 21 | 5 | ... |  wherever they are.
    The per-section cells are compared only when there is one cell per entry
    section, in page order; otherwise only the totals are checked. Any other
    layout is skipped, so the page can change shape without failing CI.
    """
    row = re.compile(r"^\|\s*\[?`([^`]+)`(?:\]\([^)]*\))?\s*\|\s*\*\*(\d+)\*\*\s*\|(.*)\|\s*$")
    declared = {}
    for line in text.splitlines():
        m = row.match(line.strip())
        if m:
            cells = [c.strip() for c in m.group(3).split("|")]
            declared[m.group(1)] = (int(m.group(2)), cells)
    if not declared:
        return

    sections, actual, per = [], {}, {}
    for t in tables(text):
        if not is_entry_table(t):
            continue
        if t["section"] not in sections:
            sections.append(t["section"])
        for cells in t["rows"]:
            if len(cells) < 2:
                continue
            for robot in set(re.findall(r"`([^`]+)`", cells[1])):
                actual[robot] = actual.get(robot, 0) + 1
                per[(robot, t["section"])] = per.get((robot, t["section"]), 0) + 1

    for robot, (total, cells) in declared.items():
        if actual.get(robot, 0) != total:
            report.warn("by-robot", "%s: By robot says %s %d, the tables hold %d"
                        % (path, robot, total, actual.get(robot, 0)))
        if len(cells) != len(sections):
            continue
        for sec, cell in zip(sections, cells):
            want = per.get((robot, sec), 0)
            got = int(cell) if cell.isdigit() else 0
            if got != want:
                report.warn("by-robot", "%s: By robot says %s has %d in %r, the table holds %d"
                            % (path, robot, got, sec, want))
    for robot, n in sorted(actual.items()):
        if robot not in declared:
            report.warn("by-robot", "%s: %d entries use %s, but By robot has no row for it"
                        % (path, n, robot))

    # The quick "Find by robot" table near the top, if there is one:
    #   | [**TRON1**](robots/TRON1.md) | ... |  then a row of "71 projects" cells.
    lines = text.splitlines()
    for i, line in enumerate(lines):
        names = re.findall(r"\[\*\*([^*]+)\*\*\]\(robots/", line)
        if len(names) < 2 or i + 2 >= len(lines):
            continue
        nums = re.findall(r"\d+", lines[i + 2])
        if len(nums) != len(names):
            continue
        for robot, n in zip(names, nums):
            if robot in actual and actual[robot] != int(n):
                report.warn("by-robot", "%s: Find by robot says %s %s, the tables hold %d"
                            % (path, robot, n, actual[robot]))
        break

    # The one-line summary, if there is one: "TRON1 52 · TRON2 17 · ..."
    m = re.search(r"<summary>(.*?)</summary>", text, re.S)
    if m:
        for robot, n in re.findall(r"([A-Za-z][A-Za-z0-9]*) (\d+)", m.group(1).split("</b>")[-1]):
            if robot in actual and actual[robot] != int(n):
                report.warn("by-robot", "%s: summary says %s %s, the tables hold %d"
                            % (path, robot, n, actual[robot]))


def check_contents(text, path, row_counts, report):
    """Section counts in the Contents list or nav line. Warn only.

    Recognises "[Section](#anchor) — 32" and "[Section](#anchor) (32)";
    names that are not entry sections are ignored.
    """
    for m in re.finditer(r"\[([^\]]+)\]\(#[^)]+\)\s*(?:[—–-]\s*(\d+)|[(（](\d+)[)）])", text):
        name, n = m.group(1), int(m.group(2) or m.group(3))
        if name in row_counts and row_counts[name] != n:
            report.warn("counts", "%s: Contents says %r has %d, the tables hold %d"
                        % (path, name, n, row_counts[name]))


def check_links(paths, report):
    urls = set()
    for p in paths:
        urls.update(urls_in(open(p, encoding="utf-8").read()))
    print("Checking %d external links...\n" % len(urls))
    for u in sorted(urls):
        code = fetch_code(u)
        if code >= 400 or code == 0:
            report.warn("dead-link", "%s (%s)" % (u, "HTTP %d" % code if code else "unreachable"))


def fetch_code(url):
    req = urllib.request.Request(url, headers={"User-Agent": "awesome-limx-ci"})
    try:
        return urllib.request.urlopen(req, timeout=25).getcode()
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:  # noqa: BLE001 - DNS and TLS failures are expected here
        return 0


def main():
    ap = argparse.ArgumentParser(description="Validate the awesome-limx list.")
    ap.add_argument("--check-links", action="store_true",
                    help="also fetch every external link (slow, needs network)")
    ap.add_argument("--strict", action="store_true",
                    help="treat warnings as failures")
    ap.add_argument("--root", default=".", help="repository root")
    args = ap.parse_args()

    report = Report()
    paths = [(os.path.join(args.root, p), lang) for p, lang in EDITIONS]

    editions = {}
    for path, lang in paths:
        if not os.path.exists(path):
            report.error("files", "missing %s" % path)
            continue
        text = open(path, encoding="utf-8").read()
        if "\r\r" in text:
            report.warn("newline", "%s: contains a doubled CR. Writing CRLF text "
                        "through a Windows text-mode open turns CRLF into CR CRLF, "
                        "which adds a blank line after every line" % path)
        if check_table_breaks(text, path, report):
            # The tables are broken; whatever we parsed out of them would be noise.
            continue
        entries, row_counts = check_tables(text, lang, path, report)
        check_refs(text, path, entries, report)
        check_counts(text, path, row_counts, report)
        check_contents(text, path, row_counts, report)
        check_by_robot(text, path, report)
        editions[lang] = entries

    if "en" in editions:
        en = set(editions["en"])
        for lang, other in editions.items():
            if lang == "en":
                continue
            name = dict((l, p) for p, l in EDITIONS)[lang]
            for a in sorted(en - set(other)):
                report.error("sync", "entry p-%s is in README.md but not %s" % (a, name))
            for a in sorted(set(other) - en):
                report.error("sync", "entry p-%s is in %s but not README.md" % (a, name))

    # robots/*.md are rebuilt by the robot-pages workflow after every README
    # change lands on main. A pull request, and the push that runs alongside
    # that workflow, are expected to see them behind: say nothing there. The
    # weekly scheduled run and local runs still check.
    if os.environ.get("GITHUB_EVENT_NAME") not in ("pull_request", "push"):
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            import build_robot_pages
            stale = [page for page, content in build_robot_pages.build(args.root).items()
                     if (open(page, encoding="utf-8").read() if os.path.exists(page) else None) != content]
            if stale:
                report.warn("robot-pages", "%d robot page(s) out of date (%s%s). They are rebuilt automatically after "
                            "the README change reaches main; to do it by hand: python scripts/build_robot_pages.py"
                            % (len(stale), ", ".join(os.path.basename(p) for p in stale[:4]), ", ..." if len(stale) > 4 else ""))
        except Exception as e:  # the page builder is a convenience, never a blocker
            report.warn("robot-pages", "could not check robot pages: %s" % e)

    if args.check_links:
        check_links([p for p, _ in paths if os.path.exists(p)], report)

    return report.dump(args.strict)


if __name__ == "__main__":
    sys.exit(main())
