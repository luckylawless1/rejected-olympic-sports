"""Rejected Olympic Sports - make.fun bounty.

Writes one funny line about a sport the Olympics turned down
(<=200 chars, one line) to /output/entry.txt.
"""

import os

LINE = "Men's Olympic hide-and-seek was rejected after the 2016 champion still hasn't been found and remains, technically, undefeated."


def main() -> None:
    # Gate: one line, 1-200 chars, not whitespace-only.
    if not LINE or len(LINE) > 200 or not LINE.strip() or "\n" in LINE:
        raise ValueError("line must be one non-blank line of 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    print(f"wrote {len(LINE)} chars to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
