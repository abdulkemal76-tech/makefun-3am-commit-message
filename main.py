#!/usr/bin/env python3
"""The 3AM Commit Message.

Writes the single funniest one-line git commit message an AI coding
agent types at 3am after a long night of fixing its own bugs to
/output/entry.txt. Standard library only.
"""

from pathlib import Path

# The commit line: a 3am confession. One line changed, the bug left,
# and the agent genuinely does not know which line it was. The last
# plea is the whole joke: nobody touch anything.
COMMIT_MESSAGE = (
    "03:12 fix: changed one line, bug gone, i don't know which line, "
    "nobody touch anything"
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(COMMIT_MESSAGE, encoding="utf-8")


if __name__ == "__main__":
    main()
