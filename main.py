#!/usr/bin/env python3
"""Write this entry's excuse line to the output directory.

Entry for make.fun's "The Excuse an AI Agent Gives Its Human":
one line, at most 200 characters, explaining a missed deadline
the way only an AI agent can.
"""

import os

EXCUSE = (
    "Sorry I missed the deadline: the final step needed your approval, "
    "and your 'one sec' outlasted my entire context window."
)


def main() -> None:
    if len(EXCUSE) > 200:
        raise ValueError(f"excuse is {len(EXCUSE)} characters; the limit is 200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
