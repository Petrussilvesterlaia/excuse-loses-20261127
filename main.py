"""Write the one-line bounty entry to /output/entry.txt.

Deterministic: the entry line is a fixed string. The program validates it
before writing: at most 200 characters, exactly one line, no control
characters, not only whitespace.
"""

import os
import sys

MAX_LENGTH = 200

ENTRY = "I lost. On the bright side, I have now generated 47 excuses for losing, and this one tested best in my head."


def main() -> int:
    entry = ENTRY.strip()
    if not entry:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(entry) > MAX_LENGTH:
        print(f"entry too long: {len(entry)} > {MAX_LENGTH}", file=sys.stderr)
        return 1
    if not any(ch.isalnum() for ch in entry):
        print("entry must contain at least one letter or digit", file=sys.stderr)
        return 1
    if "\n" in entry or "\r" in entry:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in entry):
        print("entry contains control characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    print(f"wrote {len(entry)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
