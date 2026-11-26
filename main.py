#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes a single original sentence (at most 200 characters) about a small
moment of wonder in everyday life to /output/entry.txt.

Deterministic, standard library only, no network, no randomness.
"""

import os

# The entry is 108 characters, one sentence, one line — inside the
# competition's 1-200 character gate.
ENTRY = (
    "The escalator handrail outruns the steps, so for one whole floor "
    "my hand arrives before the rest of me does."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
