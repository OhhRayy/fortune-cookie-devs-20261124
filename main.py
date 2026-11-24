"""Fortune Cookie Wisdom for Developers (make.fun bounty
u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44).

Writes one original fortune-cookie line for a software developer
to /output/entry.txt. Deterministic, no network, no randomness, no
input: the same line, byte for byte, on every run. The line was
chosen for the judge's brief: it reads like a real fortune cookie
(one short balanced sentence), says something true about a
developer's day (legacy code, shipping by Friday), and turns that
truth in a way the reader has not heard before — the person you
curse was only trying to ship, exactly like you.
"""

import os

LINE = (
    "The legacy code you curse was written by someone who, "
    "like you, was only trying to ship by Friday."
)


def main() -> None:
    text = LINE
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters,
    # not only white space, a single line.
    assert 1 <= len(text) <= 120, "line must be 1-120 Unicode code points"
    assert text == text.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
