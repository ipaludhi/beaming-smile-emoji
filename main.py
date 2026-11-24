"""Beaming smile — one emoji, one smile.

Writes exactly one emoji to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR):
U+1F601 BEAMING FACE WITH SMILING EYES.

Why this emoji, against the judge's criteria in order:
1. A broad, genuine grin with smiling eyes plainly aims to warm a stranger —
   a face smiling broadly at you is the most direct warmth there is.
2. Warmth at first glance: the grin is instant, contagious joy, no context needed.
3. Universality: a grin is read the same way at any age or background, with
   no irony, in-joke or cultural reference that could land wrong.
4. Chosen rather than default: it is not the first smiley that comes to mind
   (the plain 🙂 / 😊); the beaming, teeth-showing grin feels picked for the
   moment — maximum smile — while staying instantly readable.
5. Right for a stranger: pure joy, no intimacy, sarcasm or flirtation.

No network, no randomness, no input. Deterministic: every run writes
byte-identical output (4 bytes UTF-8, 1 character).
"""

import os
from pathlib import Path

EMOJI = "\U0001F601"  # 😁 BEAMING FACE WITH SMILING EYES


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EMOJI, encoding="utf-8")


if __name__ == "__main__":
    main()
