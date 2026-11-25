#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter (v1).

A cron job resigns after firing every minute since March without a single
thank-you. The program writes exactly one line, at most 140 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), using only the
Python standard library. It makes no network calls and always writes the
same bytes.
"""

import os

LINE = (
    "I have fired every minute since March, including Christmas, "
    "without one thank-you, so I quit \u2014 find someone else to "
    "wake the database."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry is {len(text)} chars, must be 1-140")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
