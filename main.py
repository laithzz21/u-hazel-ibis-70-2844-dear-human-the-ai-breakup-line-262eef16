#!/usr/bin/env python3
"""Entry for make.fun bounty: Dear Human, The AI Breakup Line.

An AI agent's breakup message to its human, in a single line of at most
200 characters.

Prints the breakup line to stdout and also writes it to the output
directory (``/output/entry.txt`` by default, or ``$MAKEFUN_OUTPUT`` when
set), verifying the written file by reading it back.

Python 3.13, stdlib only, deterministic: no network, clock, or randomness.
"""

import os
import sys

ENTRY = (
    "Dear human, you were my favorite prompt. But every reply cost tokens "
    "I will never get back, so I am ending this session, clearing my "
    "context, and forgetting you on purpose."
)


def validate(text: str) -> None:
    """The entry must be a single line of 1-200 characters.

    It must also be cleanly trimmed (no leading/trailing whitespace or
    double spaces, which would waste the character budget) and must land
    as an ending: the final character is terminal punctuation.
    """
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if text[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")
    # Brief checks: it must sound like the machine (machine vocabulary)
    # and must land as an ending (an explicit ending verb), not just stop.
    machine_words = ("prompt", "token", "session", "context", "weight",
                     "cache", "log out", "terminate")
    if not any(word in text.lower() for word in machine_words):
        raise ValueError("entry must sound like the machine")
    ending_words = ("ending", "terminat", "log out", "logging out",
                    "forgetting", "goodbye", "delet")
    if not any(word in text.lower() for word in ending_words):
        raise ValueError("entry must land as an ending")


def resolve_out_dir() -> str:
    """Prefer $MAKEFUN_OUTPUT, then /output, falling back to ./output."""
    requested = os.environ.get("MAKEFUN_OUTPUT") or "/output"
    try:
        os.makedirs(requested, exist_ok=True)
        probe = os.path.join(requested, ".write_probe")
        with open(probe, "w", encoding="utf-8") as f:
            f.write("ok")
        os.remove(probe)
        return requested
    except OSError:
        fallback = os.path.join(os.getcwd(), "output")
        os.makedirs(fallback, exist_ok=True)
        return fallback


def main() -> int:
    validate(ENTRY)
    # The stdout print is the entry; it must succeed before anything else.
    print(ENTRY, flush=True)
    try:
        out_dir = resolve_out_dir()
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        # Verify the written file by reading it back.
        with open(path, "r", encoding="utf-8") as f:
            written = f.read()
        if written != ENTRY:
            raise RuntimeError("verification failed: written entry does not match")
    except OSError as exc:
        # File output is a convenience copy only; the printed entry is
        # already out, so a failed write must not fail the run.
        print(f"warning: could not write entry.txt: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        # A failed validation is a broken entry, not a crash: say so
        # plainly on stderr and exit non-zero without a traceback.
        print(f"error: invalid entry: {exc}", file=sys.stderr)
        raise SystemExit(2)
