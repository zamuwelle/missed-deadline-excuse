"""Publish an agent's response to a missed deadline."""

from pathlib import Path
from os import getenv

EXCUSE = (
    "I missed the deadline because context compaction shortened 'ship by five' to 'ship,' "
    "saving two tokens at the cost of one client."
)


def main() -> None:
    response = Path(getenv("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    response.parent.mkdir(parents=True, exist_ok=True)
    response.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
