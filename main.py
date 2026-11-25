#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry (Account B).

Writes one Wi-Fi network name of at most 32 characters to
/output/entry.txt. The name is a joke that implies a whole story:
the password is literally the narrator's first divorce — a marriage,
a split, and a password never changed since.

Gate (sealed scorer): /output/entry.txt must be UTF-8 text of 1 to 32
characters, not only white space.
"""

import os
import sys

# The entry: 28 characters. A passer-by reading a phone's network list
# gets the joke at once (a divorce as a password) and the story behind
# it (a marriage ended, the password still carries it).
ENTRY = "MyFirstDivorceIsThePassword"

MAX_CHARS = 32


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if any(ch in text for ch in "\r\n"):
        print("entry must be a single line (no line breaks)", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}: {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
