# Studying in this repo (for Claude chats)

This repo is the backend for study chats. Jacob works up his classes in a corkscrew and logs, per problem, the
understanding he had to get before he could do it. `brain school` writes those files, commits only them, and pushes;
you never hand-edit them.

## Start of a session
1. `brain school` says where he is: the lecture (with its PDF paths), what comes next, and the hang-ups already
   logged on this lecture. Open the lecture PDF it names (look at page images for math, not only pdftotext).
2. Teach from the floor: the notation and arithmetic the lecture assumes, then climb. Every math step: what is
   given, what changes, what the next step receives. Plain words. Use the `teach` skill if he asks to be taught.

## While he works
- He gets stuck on a problem and you find the missing understanding:
  `brain school stuck "<the understanding, a short phrase>" --problem P3`
  (defaults to the current lecture; add `--item HW1` or `--item "Discussion 7"`, `--course STAT132` for others).
- It rests on something deeper he also lacks: `brain school stuck "<deeper phrase>" --under n3`.
- He shows he has it (explains it back, or solves with it): `brain school got n3`. That is his own word, not a rep.
  Graded practice still goes to `brain study log "<Concept>" problem solved|easy|hint|failed`.
- He finishes the lecture: `brain school done` (the next class comes up; `brain school skip` passes one).
- `brain school needs [STAT132]` prints the graph as text.

Each of those commits and pushes by itself. Do not `git add` or commit `study/`, `CORKSCREW.md` or `*/NEEDS.md`
yourself, and never `git add -A` here: the nightly sync leaves its own uncommitted work in this tree.

## Files
- `CORKSCREW.md`: where he is and the whole order (one lecture per class in turn, the class furthest behind first).
- `<COURSE>/NEEDS.md`: per lecture or assignment, each problem and what it rested on, as a graph (red open, green got).
- `study/path.csv`, `study/needs.csv`: the data behind both. Generated pages say "do not edit"; believe them.
- Everything else (files/, notes/, PROGRESS.md, assignments/) comes from `sync.py`; see README.md.
