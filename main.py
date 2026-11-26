"""Robot vacuum's excuse for missing a spot.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic: stdlib only, no randomness, no network, no clock.
"""

import os

ENTRY = (
    # The vacuum's excuse: low battery, cable-eating, stuck under the couch.
    "I was three percent from the dock when your charging cable "
    "looked delicious, so I ate it and died under the couch."
)

assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
