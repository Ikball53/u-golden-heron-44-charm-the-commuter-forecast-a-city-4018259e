#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes a single-line weather forecast for a fictional city to
/output/entry.txt, with no trailing newline.

The line names the place, gives it weather, and tries to make a bored
commuter smile: a sunny forecast undercut by a precisely timed,
four-minute shower, then a second beat where the umbrella gets left
on the bus.
"""

from pathlib import Path

ENTRY = (
    "Today in Nowhereville: sunny, 22°, with a 4-minute shower at 7:03 "
    "— pack an umbrella, leave it on the bus, smile at the sun."
)

MAX_LENGTH = 140
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_LENGTH, (
        f"entry is {len(ENTRY)} chars, must be 1-{MAX_LENGTH}"
    )
    assert "\n" not in ENTRY, "entry must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
