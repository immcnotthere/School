#!/usr/bin/env python3
"""Refresh this repo from the laptop. One-way (laptop -> repo). Only notes/ is a mirror (a note that moved or left
the vault leaves notes/ too; git history keeps it); nothing else here is ever deleted.

Usage:  python3 -I sync.py        # then review `git status` and commit

1. notes/            course notes from the Obsidian vault (the source of truth): a file goes in when its path names
                     a course OR its frontmatter says `course:` one. PDFs, zips, .obsidian, .claude, System/ (90 System), Personal/Daily and Weekly skipped.
2. <COURSE>/files/   mirror of ~/Documents/<COURSE> (lectures, homework, exams, readings, textbook, transcripts).
                     Audio/video and anything over 50 MB stay on the laptop (GitHub rejects big files).
   Subfolders are renamed to the standard set (course-info, lectures, homework, exams, readings, textbook,
                     recordings, review, prereqs, other) by assignments.remap.
4. <COURSE>/assignments/  per-assignment status (hand-edited status.csv), index, dependency map (assignments.py).
3. <COURSE>/PROGRESS.md, <COURSE>/progress.csv, <COURSE>/reps.csv
                     study progress from brain: the rep ledger `System/reps.csv` replayed through brain's FSRS
                     model (the installed copy in ~/.local/lib/brain), so the numbers match the Brain window.
"""
import csv
import hashlib
import os
import re
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from assignments import build as build_assignments, remap  # noqa: E402
VAULT = os.path.expanduser("~/Documents/Second Brain")
DOCS = os.path.expanduser("~/Documents")
BRAIN = os.path.expanduser("~/.local/lib/brain")
# repo folder -> course names used in vault frontmatter / brain
COURSES = {"AM20": ["AM 20"], "STAT132": ["STAT 132"], "ECON131": ["ECON 131"]}
TERM_START = date(2026, 9, 21)  # Monday of week 0
MAX_BYTES = 50 * 1024 * 1024
MEDIA = re.compile(r"\.(m4a|mp3|wav|aac|ogg|flac|mp4|mov|mkv|webm)$", re.I)


# ---------------------------------------------------------------- 1. vault notes
KEEP = re.compile(r"(stat(s)? ?(131|132)|econ ?(104|131|140)|\bam ?(10|20)|am20|international ?financial"
                  r"|^(am20|stats 131|canvas decks|computer science|differential equations)/)", re.I)
SKIP = re.compile(r"\.(pdf|zip|deckssynclog)$|^\.obsidian|^\.claude|^(90 )?System/|^Personal/(Daily|Weekly)/|Diary|Philosoph", re.I)
COURSE_FM = re.compile(r"^course:\s*[\"'\[]*\s*(am ?(10|20)|stats? ?13[12]|econ ?(104|131|140)|econometrics)\b",
                       re.I | re.M)


def frontmatter(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            head = f.read(4000)
    except OSError:
        return ""
    if not head.startswith("---"):
        return ""
    end = head.find("\n---", 3)
    return head[:end] if end > 0 else ""


def sync_notes():
    files = subprocess.check_output(["git", "-C", VAULT, "ls-files", "-z"]).decode().split("\0")
    n, kept = 0, set()
    for f in files:
        if not f or SKIP.search(f):
            continue
        src = os.path.join(VAULT, f)
        if not KEEP.search(f) and not (f.endswith(".md") and COURSE_FM.search(frontmatter(src))):
            continue
        if not os.path.isfile(src):
            continue
        out = os.path.join(ROOT, "notes", f)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        shutil.copy2(src, out)
        kept.add(os.path.normpath(out))
        n += 1
    gone = 0
    if n:       # never empty the snapshot because the vault could not be read
        for d, dirs, names in os.walk(os.path.join(ROOT, "notes"), topdown=False):
            for name in names:
                if os.path.normpath(os.path.join(d, name)) not in kept:
                    os.remove(os.path.join(d, name))
                    gone += 1
            if d != os.path.join(ROOT, "notes") and not os.listdir(d):
                os.rmdir(d)
    print(f"notes: {n} vault files" + (f", {gone} copies of moved or removed notes dropped" if gone else ""))


# ---------------------------------------------------------------- 2. course files
def sync_files():
    left = []
    for code in COURSES:
        src_root, n = os.path.join(DOCS, code), 0
        for d, _, names in os.walk(src_root):
            for name in names:
                src = os.path.join(d, name)
                rel = os.path.relpath(src, src_root)
                if MEDIA.search(name) or os.path.getsize(src) > MAX_BYTES:
                    left.append(f"{code}/{rel}")
                    continue
                out = os.path.join(ROOT, code, "files", remap(rel))
                os.makedirs(os.path.dirname(out), exist_ok=True)
                shutil.copy2(src, out)
                n += 1
        print(f"files: {code} {n}")
    for x in left:
        print(f"  left on laptop (audio or >50 MB): {x}")


# ---------------------------------------------------------------- 3. progress
def sq(p):
    """Heat square for a recall probability (None = never studied)."""
    if p is None:
        return "⬜"
    return "🟩" if p >= 0.9 else "🟨" if p >= 0.7 else "🟧" if p >= 0.4 else "🟥"


def day_sq(n):
    return "⬜" if n == 0 else "🟨" if n < 10 else "🟧" if n < 30 else "🟩"


def lecture(source):
    s = re.sub(r"\s*p\.?\s*\d*\s*$", "", source or "").strip()
    return s or "(no source)"


def mid(name):
    return "n" + hashlib.md5(name.encode()).hexdigest()[:10]


def label(s):
    return s.replace('"', "#quot;").replace("[", "(").replace("]", ")")


def sync_progress():
    sys.path.insert(0, BRAIN)
    from brain import core, study  # noqa: E402  (brain's own model, so numbers match the app)

    cmap = study.concepts()
    model = study.replay(cmap)
    memory = model["memory"]
    rows = study.read_reps()
    now = core.now()
    by_node = defaultdict(list)
    for r in rows:
        by_node[r["node"].lower()].append(r)
    exams = study.exams(cmap)

    for code, names in COURSES.items():
        own = [k for k, v in cmap.items() if v["course"] in names]
        keys, stack = set(own), list(own)
        while stack:  # pull in every prerequisite, whatever course it belongs to
            for n in cmap.get(stack.pop(), {}).get("needs", []):
                if n.lower() not in keys:
                    keys.add(n.lower())
                    stack.append(n.lower())
        keys = {k for k in keys if k in cmap}

        # prerequisites first (topological), then by lecture and name
        order, done = [], set()

        def visit(k, path=()):
            if k in done or k in path:
                return
            for n in sorted(cmap[k]["needs"], key=str.lower):
                if n.lower() in keys:
                    visit(n.lower(), path + (k,))
            done.add(k)
            order.append(k)

        for k in sorted(keys, key=lambda k: (cmap[k]["course"] not in names, lecture(cmap[k]["source"]), k)):
            visit(k)

        info = {}
        for k in order:
            c, mem, reps = cmap[k], memory.get(k, {}), by_node.get(k, [])
            last = max((r["ts"] for r in reps), default="")
            facet = {}
            for f in study.FACETS:
                m = mem.get(f)
                facet[f] = None if not m else {"r": study._r_now(m), "due": study._due_at(m).date().isoformat(),
                                               "s": m["s"]}
            info[k] = {"name": c["name"], "course": c["course"] or "(none)", "lecture": lecture(c["source"]),
                       "needs": [n for n in c["needs"] if n.lower() in keys], "reps": len(reps),
                       "first": min((r["ts"] for r in reps), default="")[:10], "last": last[:10],
                       "days": (now.date() - date.fromisoformat(last[:10])).days if last else None, **facet}

        def p(i, f):
            return i[f]["r"] if i[f] else None

        # progress.csv: one row per concept, machine-readable
        with open(os.path.join(ROOT, code, "progress.csv"), "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["concept", "course", "lecture", "needs", "reps", "first_studied", "last_studied",
                        "days_since", "recall_now", "recall_due", "recall_stability_days", "use_now", "use_due",
                        "use_stability_days"])
            for k in order:
                i = info[k]
                w.writerow([i["name"], i["course"], i["lecture"], "; ".join(i["needs"]), i["reps"], i["first"],
                            i["last"], "" if i["days"] is None else i["days"]]
                           + sum(([round(i[f]["r"], 3), i[f]["due"], round(i[f]["s"], 2)] if i[f] else ["", "", ""]
                                  for f in study.FACETS), []))

        # reps.csv: this course's slice of the ledger
        with open(os.path.join(ROOT, code, "reps.csv"), "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=study.FIELDS, extrasaction="ignore")
            w.writeheader()
            for r in rows:
                if r["node"].lower() in keys:
                    w.writerow(r)

        # PROGRESS.md
        studied = [k for k in order if info[k]["reps"]]
        L = [f"# {code} progress (generated by sync.py, do not edit)", "",
             f"Updated {now:%Y-%m-%d %H:%M}. {len(studied)} of {len(order)} concepts studied "
             f"({len(own)} {code} concepts plus {len(order) - len(own)} prerequisites from other courses). "
             "Source: brain's rep ledger (`System/reps.csv` in the vault) replayed through FSRS-6. "
             "Machine-readable: [progress.csv](progress.csv), raw reps: [reps.csv](reps.csv).", "",
             "**Key.** Recall/use now: ⬜ never studied · 🟥 under 40% · 🟧 40-69% · 🟨 70-89% · 🟩 90%+. "
             "A memory shows at most 30% until a free-recall success an hour or more later proves it, and 0 after a "
             "miss. *Recall* = produce the definition from memory; *use* = solve a problem with it.", ""]

        L += ["## Exams", "", "| exam | date | in scope | studied | ready on the day |", "|---|---|---|---|---|"]
        for e in exams:
            if e["course"] not in names:
                continue
            at = datetime.combine(e["date"], datetime.min.time(), core.tz())
            n = len(e["nodes"])
            seen = sum(1 for x in e["nodes"] if x.lower() in memory)
            ready = sum(study._readiness(memory.get(x.lower(), {}), at) for x in e["nodes"]) / n if n else 0
            L.append(f"| {e['name']} | {e['date']} | {n} | {seen} | {round(100 * ready)}% |")
        L.append("")

        # calendar heatmap of reps on this course's concepts
        days = Counter(r["ts"][:10] for r in rows if r["node"].lower() in keys)
        weeks = max(0, (now.date() - TERM_START).days // 7) + 1
        L += ["## When I studied", "", "Reps per day on these concepts: ⬜ 0 · 🟨 1-9 · 🟧 10-29 · 🟩 30+", "",
              "| | " + " | ".join(f"W{w}" for w in range(weeks)) + " |", "|---" * (weeks + 1) + "|"]
        for d in range(7):
            cells = []
            for w in range(weeks):
                day = TERM_START + timedelta(days=7 * w + d)
                cells.append(" " if day > now.date() else day_sq(days.get(day.isoformat(), 0)))
            L.append(f"| {'MTWTFSS'[d]} | " + " | ".join(cells) + " |")
        L += ["", f"Week 0 starts {TERM_START}. Total reps: {sum(days.values())} on "
              f"{len(days)} days.", ""]

        # what to do next
        due = sorted((k for k in studied if any(info[k][f] and info[k][f]["due"] <= now.date().isoformat()
                                                 for f in study.FACETS)),
                     key=lambda k: min(p(info[k], f) or 0 for f in study.FACETS if info[k][f]))
        ready_new = [k for k in order if not info[k]["reps"] and all(info[n.lower()]["reps"] for n in info[k]["needs"])]
        L += ["## Next", "", f"**Due now ({len(due)}):** " + (", ".join(info[k]["name"] for k in due[:25]) or "none")
              + (" ..." if len(due) > 25 else ""), "",
              f"**Ready to start ({len(ready_new)}), prerequisites all studied:** "
              + (", ".join(info[k]["name"] for k in ready_new[:25]) or "none") + (" ..." if len(ready_new) > 25 else ""),
              ""]

        # dependency heatmap graph (GitHub renders Mermaid)
        L += ["## Dependency heatmap", "", "Arrows go from a prerequisite to the concept that needs it. Colour = recall now.",
              "", "```mermaid", "flowchart LR"]
        groups = defaultdict(list)
        for k in order:
            groups[info[k]["lecture"]].append(k)
        for gi, (g, ks) in enumerate(sorted(groups.items())):
            L.append(f'  subgraph g{gi}["{label(g)}"]')
            for k in ks:
                L.append(f'    {mid(k)}["{label(info[k]["name"])}"]:::{ {"⬜": "none", "🟥": "red", "🟧": "orange", "🟨": "yellow", "🟩": "green"}[sq(p(info[k], "recall"))] }')
            L.append("  end")
        for k in order:
            for n in info[k]["needs"]:
                L.append(f"  {mid(n.lower())} --> {mid(k)}")
        L += ["  classDef none fill:#eeeeee,stroke:#999,color:#333", "  classDef red fill:#f4a6a6,stroke:#b33,color:#000",
              "  classDef orange fill:#f8c58c,stroke:#c70,color:#000", "  classDef yellow fill:#f6e58d,stroke:#aa0,color:#000",
              "  classDef green fill:#9be29b,stroke:#3a3,color:#000", "```", ""]

        # table, prerequisites first
        L += ["## Every concept (prerequisites first)", "",
              "| recall | use | concept | lecture | last studied | days ago | reps | next due | needs |",
              "|---|---|---|---|---|---|---|---|---|"]
        for k in order:
            i = info[k]
            dues = [i[f]["due"] for f in study.FACETS if i[f]]
            needs = ", ".join(f"{sq(p(info[n.lower()], 'recall'))} {n}" for n in i["needs"])
            L.append(f"| {sq(p(i, 'recall'))} {'' if p(i, 'recall') is None else str(round(100 * p(i, 'recall'))) + '%'} "
                     f"| {sq(p(i, 'use'))} {'' if p(i, 'use') is None else str(round(100 * p(i, 'use'))) + '%'} "
                     f"| {i['name'].replace('|', '/')} | {i['lecture']} | {i['last'] or '-'} "
                     f"| {'' if i['days'] is None else i['days']} | {i['reps']} | {min(dues) if dues else '-'} "
                     f"| {needs.replace('|', '/')} |")
        with open(os.path.join(ROOT, code, "PROGRESS.md"), "w") as fh:
            fh.write("\n".join(L) + "\n")
        print(f"progress: {code} {len(studied)}/{len(order)} studied, {len(due)} due")


if __name__ == "__main__":
    sync_notes()
    sync_files()
    sync_progress()
    build_assignments(ROOT, COURSES, BRAIN)
