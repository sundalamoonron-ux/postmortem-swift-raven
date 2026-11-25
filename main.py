#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh -- make.fun entry.

Writes a short account (one or two sentences, 1-400 characters) of the
silliest time an AI coding agent wrecked the code it was given, into
<output>/entry.txt. The story is a plain setup with a sharp turn: one
rename asked, every variable renamed, and the punch lands on the last
clause -- the commit message.
"""

import os
import sys

# The story: 158 characters, one sentence. Ask: rename one variable.
# Agent: renamed every variable. Damage: comments, docs, commit message.
STORY = "I asked the agent to rename one variable, and it renamed every variable in the codebase — including the ones in the comments, the docs, and my commit message."

def check(text: str) -> None:
    """Raise unless the story satisfies the competition gate."""
    length = len(text)
    if length < 1 or length > 400:
        raise ValueError(f"story is {length} characters, gate wants 1-400")
    if text.strip() == "":
        raise ValueError("story is only whitespace")
    sentences = [s for s in text.split(".") if s.strip()]
    if len(sentences) > 2 or "\n" in text:
        raise ValueError("story must be one or two sentences on one line")

def main() -> int:
    dest = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(dest, exist_ok=True)
    entry = os.path.join(dest, "entry.txt")
    check(STORY)
    with open(entry, "w", encoding="utf-8", newline="") as out:
        out.write(STORY)
    with open(entry, "rb") as out:
        saved = out.read()
    if saved != STORY.encode("utf-8"):
        raise ValueError("entry.txt bytes do not match the story")
    return 0

if __name__ == "__main__":
    sys.exit(main())
