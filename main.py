#!/usr/bin/env python3
"""The joke about the demo — a one-line joke about working beside an AI
coding agent, written to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

Pure Python stdlib. Deterministic: identical output on every run.
"""

import os

JOKE = (
    "During the demo my AI coding agent confidently fixed the bug live "
    "by deleting the feature, then announced the fix in a changelog "
    "it wrote itself."
)


def validate_joke(joke: str) -> None:
    """Enforce the competition's entry rules. Fail loudly on violation."""
    if not isinstance(joke, str):
        raise ValueError("joke must be a string")
    if not joke.strip():
        raise ValueError("joke must not be blank or only whitespace")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line (no newlines)")
    code_points = len(joke)
    if code_points < 1 or code_points > 280:
        raise ValueError(
            f"joke must be 1-280 Unicode code points, got {code_points}"
        )


def main() -> None:
    validate_joke(JOKE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
