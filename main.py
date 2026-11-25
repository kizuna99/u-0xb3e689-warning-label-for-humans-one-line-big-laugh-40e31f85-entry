# SPDX-License-Identifier: MIT
"""Write the warning-label entry to the output directory."""
import os
from pathlib import Path

LABEL = "WARNING: This human will forget why they walked into a room in three seconds, but remember what they said wrong in 2014 forever."


def main() -> None:
    # Gate guard: the label must stay a single non-empty line of 1-160 chars.
    assert 1 <= len(LABEL) <= 160 and "\n" not in LABEL and LABEL.strip()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LABEL, encoding="utf-8")


if __name__ == "__main__":
    main()
