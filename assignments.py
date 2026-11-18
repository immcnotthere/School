"""Per-assignment tracking and dependency maps, written to <COURSE>/assignments/. Called by sync.py.

Inputs (all read-only): the vault's assignment notes (question tables, via the vault's source_map.py), brain's concept
graph and FSRS memory (same model the Brain window uses).
Outputs, per course:
  assignments/INDEX.md, assignments.csv   one row per assignment: due, status, readiness, gaps (generated)
  assignments/<slug>/ASSIGNMENT.md        question -> concept -> prerequisite map, study order, gaps (generated)
  assignments/status.csv                  the ONLY hand-edited file: status, submitted, score, notes. Rows are
                                          added for new assignments and never overwritten.
"""
import csv
import hashlib
import os
import re
import sys
from collections import OrderedDict
from datetime import date, datetime

MONTHS = {m: i + 1 for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}
STATUSES = "todo working submitted graded skipped"
SCRIPTS = os.path.expanduser("~/Documents/Second Brain/90 System/scripts")


SUBDIRS = {"Course info": "course-info", "Lectures": "lectures", "Homework and discussions": "homework",
           "Exams": "exams", "Readings": "readings", "Textbook": "textbook", "Recordings": "recordings",
           "Review sheets": "review", "MATLAB": "other/matlab", "STAT 131 prereq notes": "prereqs",
           "Duplicates from Downloads": "other/duplicates"}


def remap(rel):
    """Path inside ~/Documents/<COURSE> -> path inside <COURSE>/files (standard folder names)."""
    top, _, rest = rel.partition("/")
    if not rest:
        return "other/" + rel
    return SUBDIRS.get(top, top) + "/" + rest


def sq(p):
    return "⬜" if p is None else "🟩" if p >= 0.9 else "🟨" if p >= 0.7 else "🟧" if p >= 0.4 else "🟥"


CLS = {"⬜": "none", "🟥": "red", "🟧": "orange", "🟨": "yellow", "🟩": "green"}


def mid(s):
    return "n" + hashlib.md5(s.encode()).hexdigest()[:10]


def lab(s):
    return s.replace('"', "#quot;").replace("[", "(").replace("]", ")")


def slug(name, code):
    s = re.sub(r"^(am ?20|stat ?132|econ ?131)\s*", "", name, flags=re.I)
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "assignment"


def due_from(texts):
    for t in texts:
        m = re.search(r"due ([A-Z][a-z]{2}) (\d{1,2})", t or "")
        if m and m.group(1) in MONTHS:
            return date(2026, MONTHS[m.group(1)], int(m.group(2)))
    return None


def build(root, courses, brain_path):
    sys.path.insert(0, SCRIPTS)
    sys.path.insert(0, brain_path)
    import source_map as sm
    from brain import core, study

    r, idx = sm.Resolver(), sm.concept_index()
    cmap = study.concepts()
    memory = study.replay(cmap)["memory"]
    now = core.now()
    code_of = {n.replace(" ", "").lower(): c for c, ns in courses.items() for n in ns}

    # group assignment notes: one per note, except "Problem N" notes which share one source -> one assignment
    groups = OrderedDict()
    for name, docs in sm.assignments(idx, r):
        code = code_of.get((idx[name]["course"] or "").replace(" ", "").lower())
        if not code:
            continue
        if re.match(r"^Problem \d", name):
            key = (code, "Supplementary problems: " + (docs[0] if docs else idx[name]["source"]))
        else:
            key = (code, name)
        groups.setdefault(key, []).append((name, docs))

    def p_now(k, at=None):
        m = memory.get(k, {})
        rec = m.get("recall")
        return study._r_now(rec) if rec else None

    def ready(k, at):
        return study._readiness(memory.get(k, {}), at)

    per_course = {c: [] for c in courses}
    for (code, title), notes in groups.items():
        qs, src_docs, src_text = [], [], []
        for name, docs in notes:
            n = idx[name]
            src_docs += [d for d in docs if d not in src_docs]
            src_text.append(n["source"] or "")
            rows = sm.questions(n["body"])
            if not rows and re.match(r"^Problem \d", name):
                rows = [(name.split()[1], name.split(" ", 2)[-1], list(n["uses"]))]
            qs += [(q if len(notes) == 1 else f"{name.split(' ', 2)[0]} {q}", asks, cs) for q, asks, cs in rows]
        due = due_from(src_text + [r.reg[d]["title"] if d in r.reg and "title" in r.reg[d] else "" for d in src_docs])
        at = datetime.combine(due, datetime.min.time(), core.tz()) if due and due >= now.date() else now

        # concept closure, prerequisites first
        direct = []
        for _, _, cs in qs:
            for c in cs:
                if c.lower() not in direct:
                    direct.append(c.lower())
        order, seen = [], set()

        def visit(k, path=()):
            if k in seen or k in path or k not in cmap:
                return
            for n in sorted(cmap[k]["needs"], key=str.lower):
                visit(n.lower(), path + (k,))
            seen.add(k)
            order.append(k)

        for k in direct:
            visit(k)
        missing = [c for c in direct if c not in cmap]
        depth_of = {}

        def depth(k, path=()):
            if k in depth_of:
                return depth_of[k]
            if k in path or k not in cmap:
                return 0
            d = 1 + max([depth(n.lower(), path + (k,)) for n in cmap[k]["needs"] if n.lower() in cmap] or [0])
            depth_of[k] = d
            return d

        nm = {k: cmap[k]["name"] for k in order}
        studied = [k for k in order if k in memory]
        rd = sum(ready(k, at) for k in order) / len(order) if order else 0
        weak = sorted((k for k in order if (p_now(k) or 0) < 0.7), key=lambda k: (depth(k), p_now(k) or 0))
        gaps = []
        if missing:
            gaps.append(f"{len(missing)} question concept(s) not in the graph: " + ", ".join(missing))
        noprereq = [k for k in direct if k in cmap and not cmap[k]["needs"]]
        if noprereq:
            gaps.append(f"{len(noprereq)} concept(s) with no prerequisites listed: " + ", ".join(nm.get(k, k) for k in noprereq))
        if not src_docs:
            gaps.append("assignment source document not found in the register")
        if not qs:
            gaps.append("no question table in the vault note")

        sl = slug(title if len(notes) == 1 else "supplementary-" + (src_docs[0] if src_docs else "problems"), code)
        d = os.path.join(root, code, "assignments", sl)
        os.makedirs(d, exist_ok=True)
        srcfiles = []
        for doc in src_docs:
            for s in src_text:
                m = re.search(r"Documents/" + code + r"/(.+)$", s)
                if m:
                    srcfiles.append(remap(m.group(1)))
        srcfiles = list(dict.fromkeys(srcfiles))
        L = [f"# {title} ({code})", "", "Generated by `sync.py` / `assignments.py`; do not edit. Track status in "
             "[../status.csv](../status.csv).", "",
             f"- **Due:** {due or 'not set'}", f"- **Source:** " + (", ".join(f"[{os.path.basename(s)}](../../files/{s.replace(' ', '%20')})" for s in srcfiles) or ", ".join(src_docs) or "**none**"),
             f"- **Readiness {'on the due date' if at is not now else 'now'}:** {round(100 * rd)}% "
             f"({len(studied)} of {len(order)} concepts in the chain studied)", ""]
        if gaps:
            L += ["**Gaps:**"] + [f"- {g}" for g in gaps] + [""]
        L += ["## Questions", "", "| Q | asks | concepts (recall now) |", "|---|---|---|"]
        for q, asks, cs in qs:
            cells = ", ".join(f"{sq(p_now(c.lower()))} {c}" for c in cs)
            L.append(f"| {q} | {asks.replace('|', '/')} | {cells} |")
        L += ["", "## Study order", "",
              "Prerequisites first; only what is below 70% recall or never studied. Do these top to bottom, then work the "
              "set closed-book.", "", "| # | concept | recall now | layer | taught in |", "|---|---|---|---|---|"]
        for i, k in enumerate(weak, 1):
            p = p_now(k)
            L.append(f"| {i} | {nm[k]} | {sq(p)} {'' if p is None else str(round(100 * p)) + '%'} | {depth(k)} | "
                     f"{sm.taught(r, idx, sm.canon(idx, nm[k])).replace('|', '/')} |")
        if not weak:
            L.append("| | nothing weak: every concept is at 70%+ | | | |")
        L += ["", "## Dependency map", "",
              "Question -> concept -> prerequisite (arrows point from what you need to what needs it). Colour = recall now; "
              "dashed box = concept missing from the graph.", "", "```mermaid", "flowchart LR"]
        for q, _, cs in qs:
            L.append(f'  {mid("q" + q)}(["Q {lab(q)}"]):::q')
        for k in order:
            L.append(f'  {mid(k)}["{lab(nm[k])}"]:::{CLS[sq(p_now(k))]}')
        for c in missing:
            L.append(f'  {mid(c)}["{lab(c)}"]:::missing')
        for k in order:
            for n in cmap[k]["needs"]:
                if n.lower() in seen:
                    L.append(f"  {mid(n.lower())} --> {mid(k)}")
        for q, _, cs in qs:
            for c in cs:
                if c.lower() in seen or c.lower() in missing:
                    L.append(f'  {mid(c.lower())} --> {mid("q" + q)}')
        L += ["  classDef q fill:#dbe7ff,stroke:#36c,color:#000", "  classDef none fill:#eeeeee,stroke:#999,color:#333",
              "  classDef red fill:#f4a6a6,stroke:#b33,color:#000", "  classDef orange fill:#f8c58c,stroke:#c70,color:#000",
              "  classDef yellow fill:#f6e58d,stroke:#aa0,color:#000", "  classDef green fill:#9be29b,stroke:#3a3,color:#000",
              "  classDef missing fill:#fff,stroke:#c00,stroke-dasharray:4 3,color:#c00", "```", ""]
        with open(os.path.join(d, "ASSIGNMENT.md"), "w") as fh:
            fh.write("\n".join(L))
        per_course[code].append({"assignment": title if len(notes) == 1 else f"Supplementary problems ({src_docs[0] if src_docs else '?'})",
                                 "slug": sl, "due": due.isoformat() if due else "", "questions": len(qs),
                                 "concepts": len(order), "studied": len(studied), "readiness": round(100 * rd),
                                 "weakest": "; ".join(nm[k] for k in weak[:3]), "gaps": len(gaps)})

    for code, rows in per_course.items():
        ad = os.path.join(root, code, "assignments")
        os.makedirs(ad, exist_ok=True)
        sp, status = os.path.join(ad, "status.csv"), OrderedDict()
        if os.path.exists(sp):
            for s in csv.DictReader(open(sp)):
                status[s["assignment"]] = s
        for row in rows:
            status.setdefault(row["assignment"], {"assignment": row["assignment"], "status": "todo", "due": row["due"],
                                                  "submitted": "", "score": "", "notes": ""})
        with open(sp, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["assignment", "status", "due", "submitted", "score", "notes"])
            w.writeheader()
            w.writerows(status.values())
        rows.sort(key=lambda x: (x["due"] or "9999", x["assignment"]))
        with open(os.path.join(ad, "assignments.csv"), "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["assignment", "status", "due", "questions", "concepts_in_chain", "studied", "readiness_pct", "weakest", "gaps"])
            for x in rows:
                s = status[x["assignment"]]
                w.writerow([x["assignment"], s["status"], s["due"] or x["due"], x["questions"], x["concepts"], x["studied"],
                            x["readiness"], x["weakest"], x["gaps"]])
        L = [f"# {code} assignments (generated by sync.py, do not edit)", "",
             f"Updated {now:%Y-%m-%d %H:%M}. Status values (edit [status.csv](status.csv)): {STATUSES}. "
             "Each assignment has a dependency map, a study order and its gaps.", "",
             "| assignment | status | due | readiness | studied / chain | weakest | gaps |", "|---|---|---|---|---|---|---|"]
        for x in rows:
            s = status[x["assignment"]]
            L.append(f"| [{x['assignment']}]({x['slug']}/ASSIGNMENT.md) | {s['status']} | {s['due'] or x['due'] or '-'} | "
                     f"{sq(x['readiness'] / 100)} {x['readiness']}% | {x['studied']} / {x['concepts']} | {x['weakest'] or '-'} | {x['gaps'] or '-'} |")
        with open(os.path.join(ad, "INDEX.md"), "w") as fh:
            fh.write("\n".join(L) + "\n")
        print(f"assignments: {code} {len(rows)}")
