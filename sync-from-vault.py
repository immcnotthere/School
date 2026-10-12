#!/usr/bin/env python3
"""Refresh notes/ from the Obsidian vault (the source of truth). One-way: vault -> this repo.

Usage:  python3 -I sync-from-vault.py            # copy, then review `git status`
Copies tracked vault files whose path matches a course (AM 10/20, ECON 104/131/140, STAT 131/132),
skipping PDFs, zips, sync logs, .obsidian, .claude and 90 System. Never deletes anything.
"""
import os, re, shutil, subprocess

VAULT = os.path.expanduser("~/Documents/Second Brain")
DEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes")
KEEP = re.compile(r"(stat(s)? ?(131|132)|econ ?(104|131|140)|\bam ?(10|20)|am20|international ?financial"
                  r"|^(am20|stats 131|canvas decks|computer science|differential equations)/)", re.I)
SKIP = re.compile(r"\.(pdf|zip|deckssynclog)$|^\.obsidian|^\.claude|^90 System|Diary|Philosoph", re.I)

files = subprocess.check_output(["git", "-C", VAULT, "ls-files", "-z"]).decode().split("\0")
n = 0
for f in files:
    if not f or SKIP.search(f) or not KEEP.search(f):
        continue
    out = os.path.join(DEST, f)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    shutil.copy2(os.path.join(VAULT, f), out)
    n += 1
print(f"copied {n} files into {DEST}")
