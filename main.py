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
    if joke != joke.rstrip():
        raise ValueError("joke must not have trailing whitespace")
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
    expected = (JOKE + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(expected)
    # Verify what was actually written: exact bytes, exactly one
    # trailing newline, and the stored line still passes validation.
    with open(path, "rb") as f:
        written = f.read()
    if written != expected:
        raise ValueError("entry.txt bytes differ from the validated joke")
    if not written.endswith(b"\n") or written.endswith(b"\n\n"):
        raise ValueError("entry.txt must end with exactly one trailing newline")
    validate_joke(written[:-1].decode("utf-8"))


if __name__ == "__main__":
    main()
