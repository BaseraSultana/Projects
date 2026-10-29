def get_text():
    """prompt the user to enter the text"""
    text = input("Enter the text: ")
    return text.strip()


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char = len
