
"""Count words, characters, and sentences in user-provided text."""


def get_text():
    """prompt the user to enter the text"""
    text = input("\nEnter the text: ")
    # global text
    return text.strip()


def count_words(text):
    """Return the number of whitespace-separated words in the text."""
    words = text.split()
    # global words
    return len(words)


def count_characters(text):
    """Count characters in the text, excluding spaces."""
    chars = len(text.replace(" ", ""))
    # global chars
    return chars


def count_sentences(text):
    """Count sentence-ending punctuation marks in the text."""
    sentence = 0
    for i in text:
        if i in ['.', '!', '?']:
            sentence += 1
    # global sentence
    return sentence


# def display_results():
#     print(f"Word Count: {words} ",f"Character Count: {chars} ",f"Sentence Count: {sentence})


def display_result():
    """Display word, character, and sentence counts for user-provided text."""
    text = get_text()
    words = count_words(text)
    chars = count_characters(text)
    sentences = count_sentences(text)
    result = (f"Word Count: {words} ", f"Character Count: {chars} ",
              f"Sentence Count: {sentences}")
    print("\nRESULT\n" + "\n".join(result))
