"""The One-Liner Groan-Off — one original dad joke, one line.

Pure Python standard library. Writes the entry to /output/entry.txt
with no trailing newline, then asserts the bounty gate in-process:
1-140 characters, a single line, not only whitespace.
"""

import os

JOKE = "I told the dinner roll to stop loafing around — it said it was just rising to the occasion."

MIN_CHARS = 1
MAX_CHARS = 140


def validate_written(path: str) -> str:
    """Re-read the file from disk and re-check the gate on its contents.

    The gate scores the file, not the string in memory, so the char
    count, the single-line rule and the no-trailing-newline rule are
    all verified against what was actually written.
    """
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"file is {len(text)} chars, outside the 1-140 gate"
    )
    assert text == text.strip(), "file must not start or end with whitespace"
    assert "\n" not in text and "\r" not in text, "file must hold exactly one line"
    assert not text.endswith("\n"), "file must not end with a newline"
    print(f"validated {path}: {len(text)} chars, {len(raw)} bytes, 1 line")
    return text


def main() -> None:
    text = JOKE.strip()
    assert MIN_CHARS <= len(text) <= MAX_CHARS, f"length {len(text)} outside gate"
    assert "\n" not in text and "\r" not in text, "entry must be exactly one line"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} chars)")
    validate_written("/output/entry.txt")


if __name__ == "__main__":
    main()
