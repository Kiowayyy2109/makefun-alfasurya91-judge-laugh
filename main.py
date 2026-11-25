#!/usr/bin/env python3
"""Make the AI Judge Laugh — one line about office life."""
import os

LINE = "Our standup meeting is fifteen minutes long, which is exactly fourteen minutes longer than the update and one minute shorter than the apology."
assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
