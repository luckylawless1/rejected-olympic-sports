"""Rejected Olympic Sports - make.fun bounty.

Writes one funny line about a sport the Olympics turned down
(<=200 chars, one line) to /output/entry.txt.
"""

import os

LINE = "Men's Olympic hide-and-seek was rejected after the 2016 champion still hasn't been found and remains, technically, undefeated."


def validate(line: str) -> None:
    """Self-check: the entry must be a single non-blank line of 1-200 chars."""
    assert isinstance(line, str), "entry must be text"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert line.strip(), "entry must not be whitespace-only"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    print(f"wrote {len(LINE)} chars to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
