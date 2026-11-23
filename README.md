# School

UCSC coursework, private. One folder per class:

| class | files (lectures, homework, exams, readings, textbook) | progress heatmap |
|---|---|---|
| AM 20 | [AM20/files](AM20/files) (+ hand-made study files in [AM20](AM20)) | [AM20/PROGRESS.md](AM20/PROGRESS.md) |
| STAT 132 | [STAT132/files](STAT132/files) | [STAT132/PROGRESS.md](STAT132/PROGRESS.md) |
| ECON 131 | [ECON131/files](ECON131/files) | [ECON131/PROGRESS.md](ECON131/PROGRESS.md) |

- **Corkscrew** ([CORKSCREW.md](CORKSCREW.md)): one lecture of each class in turn, the class furthest behind first,
  until every class is up to date. Per lecture or assignment, `<COURSE>/NEEDS.md` graphs what each problem rested on
  (what I had to understand to get past it). Written by `brain school` (CLI, or the strip on brain desk's Teach tab),
  which commits and pushes after every change; data in `study/`. Chats opened here follow [CLAUDE.md](CLAUDE.md).
- **Standard layout per class:** `files/{course-info,lectures,homework,exams,readings,textbook,recordings,review,prereqs,other}`,
  `assignments/` (INDEX.md, per-assignment dependency map in `<slug>/ASSIGNMENT.md`, and `status.csv`, the one file I edit by
  hand: todo / working / submitted / graded), `PROGRESS.md`, `progress.csv`, `reps.csv`, `README.md`. `sync.py` renames
  the folders from `~/Documents/<COURSE>` to these names. Dependency maps come from the vault's question tables
  (`source_map.py`) and brain's concept graph, coloured by recall.
- `notes/` is a **generated snapshot** of the course notes in my Obsidian vault (`~/Documents/Second Brain`), the source of truth: every note whose path names a course or whose frontmatter has `course:`.
- `<COURSE>/files/` mirrors `~/Documents/<COURSE>`. Lecture audio and anything over 50 MB stay on the laptop.
- `<COURSE>/PROGRESS.md` (colour heatmap of the prerequisite graph, study calendar, what is due), `progress.csv`
  (one row per concept: last studied, recall/use now, next due) and `reps.csv` (raw reps) come from brain's ledger
  `90 System/reps.csv`, replayed through brain's FSRS model.
- **Never edit generated files here.** Refresh everything on the laptop with `python3 -I sync.py`, then commit.
- **Nightly push** (`bin/school-push`, systemd user timer `school-push.timer`, 23:45, catches up after sleep): runs
  `sync.py`, commits only when notes, course files or reps really changed (overnight recall decay alone is thrown
  away), then pushes anything unpushed. Desktop alert when a run fails or nothing has succeeded for 3 days.
  `school-push status` shows the last success; log in `~/.local/share/school-push/log`.
  Install: `cp systemd/school-push.* ~/.config/systemd/user/ && systemctl --user daemon-reload && systemctl --user enable --now school-push.timer`.
- The ECON 131 textbook PDF (Bekaert and Hodrick, *International Financial Management*, 2nd ed.) was committed at the repo's start and stays at the top level.

Part of the [workspace](https://github.com/immcnotthere/workspace) index.
