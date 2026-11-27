#!/usr/bin/env python3
"""One Word for the Boss: write one word describing a boss to /output/entry.txt.

Python 3 standard library only. Deterministic: the same bytes on every run.
No network, no randomness, no input files.
"""

import os

WORD = "hovercraft"

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    # Exactly one word, no trailing newline: the gate counts characters (1-30).
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # Verify the bytes landed exactly as intended before exiting.
    with open(path, encoding="utf-8", newline="") as f:
        assert f.read() == WORD, "entry.txt does not match the word"
    assert len(WORD) == 10 and " " not in WORD, "word must be one word"


if __name__ == "__main__":
    main()
