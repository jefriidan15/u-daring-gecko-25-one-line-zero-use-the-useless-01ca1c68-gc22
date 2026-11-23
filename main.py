"""One Line, Zero Use: The Useless Superpower Sprint.

A single-sentence tiny story for the make.fun competition
``u-daring-gecko-25-one-line-zero-use-the-useless-01ca1c68``: the
entrant can hear what their houseplants are thinking, and every
single one of them is disappointed in the watering schedule. The
line is written to ``entry.txt`` inside the output directory so
the make.fun checker can read it back byte for byte.

Judging axes the line is built for:

* Funny -- the premise is absurd (telepathy, but only for
  houseplants) and the punchline is a domestic guilt trip delivered
  by a fern.
* Fresh -- the superpower is useless in a way nobody else's is:
  it only works on plants that cannot talk back, and all it reveals
  is disappointment.
* Neatly worded -- one sentence, setup and payoff in the same
  breath, with the turn landing on the last two words.
"""

from __future__ import annotations

import os
import sys

# The entry: one sentence, 114 characters.
# Byte-identical to the entry sentence; do not reword or re-punctuate.
ENTRY_LINE = (
    "I can hear what my houseplants are thinking, and every single "
    "one of them is disappointed in my watering schedule."
)

# Where the entry file lands. Override with $OUTPUT_DIR when the
# checker (or a local run) wants it somewhere else.
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def entry_text() -> str:
    """Return the entry line, exactly as it must appear on disk."""
    return ENTRY_LINE


def validate_entry(text: str) -> None:
    """Guard: the entry must be a single line, one sentence, 1-200 chars.

    Raises ValueError before anything is written, so a bad edit to
    ENTRY_LINE can never silently produce an invalid entry file.
    """
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text.strip() != text:
        raise ValueError("entry must not have leading/trailing whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def write_entry(path: str = OUTPUT_PATH) -> int:
    """Write the entry to ``path`` as UTF-8 with no trailing newline.

    Returns the number of characters written.
    """
    validate_entry(ENTRY_LINE)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_LINE)
    return len(ENTRY_LINE)


def main(argv: list[str] | None = None) -> int:
    """Write the entry and report where it went."""
    del argv  # no CLI arguments; behaviour is driven by $OUTPUT_DIR
    count = write_entry()
    print(f"Wrote {count} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
