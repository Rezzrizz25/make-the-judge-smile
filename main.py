"""Make the Judge Smile — one warm, surprising line about a small good thing today.

The entry line (chosen for the judge's published brief):
- Subject: a small good thing that happened today (explicit "today").
- Warmth: a stranger's unasked-for kindness, a gift pressed into my hand.
- Surprise: the gift is a *bruised* mango, and the stranger's saying flips the
  flaw into the point — the sweet ones hide in the ugly ones.
- Concreteness: one real detail, the bruised mango at the market, plus her words.
- Fresh wording: no greeting-card phrasing; the line is told, not summarised.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt)
with no trailing newline, so the file holds exactly the judged text.
"""

import os

ENTRY = (
    "A stranger at the market pressed a bruised mango into my hand today "
    "and said, 'the sweet ones hide in the ugly ones.'"
)


def main() -> None:
    # Gate self-check: the sealed scorer accepts UTF-8 text of 1-200 chars,
    # not only whitespace, as a single line. Fail loudly instead of writing
    # an entry the judge would never see.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    ENTRY.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Verify what was actually written, not just what we meant to write.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from ENTRY"


if __name__ == "__main__":
    main()
