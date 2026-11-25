"""The Funniest One-Line Resignation Letter.

Writes the one-line resignation letter of a cron job to /output/entry.txt.
Standard library only (Python 3.13).
"""

import os

LETTER = (
    "I have run every minute since March, including Christmas, "
    "and the only one who ever noticed me was the log file. I quit."
)


def main() -> None:
    # Gate mirror: the sealed scorer requires UTF-8 text of 1-140 chars,
    # not only white space. Fail loudly here rather than ship an invalid line.
    assert 1 <= len(LETTER) <= 140, f"letter is {len(LETTER)} chars"
    assert LETTER.strip(), "letter is only white space"
    assert "\n" not in LETTER, "letter must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
