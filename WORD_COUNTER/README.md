# Word Counter

A small command-line Python program for counting words, characters, and sentences in text.

## Features

- Count words, characters, sentences, or all three at once.
- Enter or paste text spanning multiple lines.
- Preserve blank lines between paragraphs. Three consecutive empty lines finish text entry.
- Type `Q` at the text prompt to return to the menu.
- Choose whether spaces are included in the character count.

## Requirements

- Python 3
- No third-party packages are required.

## Run the program

Open a terminal in this folder and run:

```powershell
python main.py
```

If `python` is not recognized on Windows, try:

```powershell
py main.py
```

Choose an option from the menu:

1. Count words
2. Count characters
3. Count sentences
4. Count all
5. Exit

At the text prompt, type or paste your text. Press Enter on three consecutive empty lines to finish. One or two empty lines can separate paragraphs. When counting characters, choose whether to include spaces.

## How counting works

- **Words:** splits the text on whitespace and counts the resulting parts.
- **Characters:** counts all characters when spaces are included. When spaces are excluded, it removes ordinary space characters before counting.
- **Sentences:** counts runs of sentence-ending punctuation (`.`, `!`, or `?`) as one sentence. For example, `?!` counts as one.

## Project structure

```text
WORD_COUNTER/
├── main.py
└── README.md
```

## Future improvements

- Make text entry easier to finish while still preserving paragraph breaks, for example by accepting an explicit end marker.
- Improve input validation so invalid character-count choices are re-prompted cleanly.
- Expand character-count options to handle tabs, newlines, and all whitespace consistently.
- Improve sentence detection for abbreviations and other punctuation edge cases.
- Add automated tests for counting and interactive input behavior.

## Author

**Basera Sultana**