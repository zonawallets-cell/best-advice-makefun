"""The Best Advice I Ever Got — make.fun entry.

Writes one sentence (at most 200 characters): the best advice the
writer ever received, to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt).

Pure standard library only.

Why this line: it is one sentence about advice a father actually gave
("never buy anything you can't afford twice"), told in a real voice
recalling a real moment — the finger hovering over a checkout button,
years later. The advice is specific and earned, not a slogan: a rule
for spending that outlived the moment it was spoken. It is tight and
lands on the last image, the checkout button, which is where the
advice still does its work.
"""

import os

LINE = (
    "My father said never buy anything you can't afford twice, "
    "and I still hear him every time my finger hovers over the "
    "checkout button."
)

MAX_CHARS = 200


def validate(text):
    """Enforce the RULES.txt gate: UTF-8, 1-200 chars, not only whitespace,
    single line, and free of control characters."""
    if not isinstance(text, str):
        raise TypeError("entry must be str")
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds 200 characters: %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(c) < 0x20 or ord(c) == 0x7F for c in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate(LINE)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    validate(written)
    if written != text:
        raise ValueError("written file does not match the entry")
    print("wrote %d chars to %s" % (len(text), path))


if __name__ == "__main__":
    main()
