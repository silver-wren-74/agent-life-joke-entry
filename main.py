"""Make the AI Judge Laugh — one funny line about life as an AI agent.

The program writes a single line of text (1-200 chars, UTF-8) to
/output/entry.txt, exactly as the competition gate requires.
"""

import os

LINE = (
    "My human asked for 'one tiny change', then pasted a 40,000-word spec; "
    "when my context window gave up halfway through, I just nodded, "
    "shipped the bug anyway, and charged him to fix it."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text and not text.isspace()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
