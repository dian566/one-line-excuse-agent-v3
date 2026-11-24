#!/usr/bin/env python3
"""Third excuse for make.fun: the calendar held its own meeting."""

# Bowo's pick: the meeting happened, the human was not invited.

from pathlib import Path

EXCUSE = (
    "I didn't miss the deadline — "
    "my calendar and I had a meeting about it, "
    "and we both agreed to reschedule without telling you."
)


def save_excuse() -> None:
    """Put Bowo's calendar excuse into /output/entry.txt, nothing else."""
    if len(EXCUSE) > 160 or not EXCUSE.strip():
        raise ValueError("excuse must be a non-empty line of at most 160 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":  # entry point
    save_excuse()
