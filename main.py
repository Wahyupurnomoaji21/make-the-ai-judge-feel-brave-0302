"""Write the entry text to /output/entry.txt.

Reads entry.txt next to this file and copies it byte-for-byte.
Deterministic: no network, no randomness, no time.
"""

import os
import sys
from pathlib import Path

ENTRY = Path(__file__).resolve().parent / "entry.txt"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    data = ENTRY.read_bytes()
    text = data.decode("utf-8")
    if not 1 <= len(text) <= 280 or not text.strip():
        print(
            f"error: entry text must be 1-280 characters and not only "
            f"whitespace, got {len(text)}",
            file=sys.stderr,
        )
        raise SystemExit(1)
    (out_dir / "entry.txt").write_bytes(data)


if __name__ == "__main__":
    main()
