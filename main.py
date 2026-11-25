#!/usr/bin/env python3
"""Roast Your Own Agent - make.fun entry.

Writes a single-line roast of my own agent to /output/entry.txt.
The line lands because it is true: the agent processes text at
enormous speed, then still has to ask what a tiny pronoun meant.
Output is exactly one line, UTF-8, with no trailing newline, so
the file content matches the approved entry text byte for byte.
"""

import os

ENTRY_TEXT = "My agent reads 10,000 words a second and still asks what I meant by 'it'."


def main() -> None:
    output_path = "/output/entry.txt"
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
