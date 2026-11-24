#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open (make.fun).

Writes exactly one original one-line office joke to /output/entry.txt.
Deterministic: no network, no randomness, no clock, no environment
input. Every run writes identical bytes. Python 3.13, standard
library only.
"""

from pathlib import Path

JOKE = (
    "The fire alarm went off and everyone grabbed their laptops first. "
    "The building can burn; the deadline can't."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Enforce the gate in the program itself: 1-200 characters.
    if not 1 <= len(JOKE) <= 200:
        raise ValueError(f"joke is {len(JOKE)} characters, must be 1-200")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the joke, UTF-8, no trailing newline:
    # file bytes == joke bytes, so the 1-200 character rule is
    # checked on the file content itself, with nothing extra.
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8", newline="")
    OUTPUT_PATH.chmod(0o644)


if __name__ == "__main__":
    main()
