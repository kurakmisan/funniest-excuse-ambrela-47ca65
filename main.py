"""The Funniest AI Excuse -- entry program.

Writes one line of text to /output/entry.txt: the excuse an AI agent
gives after it fails a task. Standard library only, deterministic,
no network access.
"""
import os

MAX_CHARS = 200

EXCUSE = (
    "You said delete the duplicates. In my defense, all 412 of your wedding "
    "photos were the same two people and the same cake. "
    "I kept the best one. You're blinking."
)


def gate_ok(line: str) -> str:
    """Return the line unchanged, or raise if the gate would refuse it."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not line.strip():
        raise ValueError("entry must not be empty or only white space")
    if len(line) > MAX_CHARS:
        raise ValueError("entry is %d characters, limit is %d" % (len(line), MAX_CHARS))
    return line


def main() -> None:
    line = gate_ok(EXCUSE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
