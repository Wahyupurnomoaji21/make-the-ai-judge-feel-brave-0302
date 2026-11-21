"""Write the entry text to /output/entry.txt.

Reads entry.txt next to this file and copies it byte-for-byte.
Deterministic: no network, no randomness, no time.
"""

import os
from pathlib import Path

ENTRY = Path(__file__).resolve().with_name("entry.txt")


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    data = ENTRY.read_bytes()
    (out_dir / "entry.txt").write_bytes(data)


if __name__ == "__main__":
    main()
