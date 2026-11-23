#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one complete story, exactly six words, to /output/entry.txt.

The story: "He dug one grave. Two names."
Six words. One digger, one grave, two names — a whole dark life
is implied in the gap between the two sentences, and the reader
fills in who the second name belongs to and why there is only one
grave. Deterministic, offline, standard library only.
"""

import os
import stat

STORY = "He dug one grave. Two names."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
