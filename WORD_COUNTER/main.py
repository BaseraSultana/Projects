def get_text():
    """prompt the user to enter the text"""
    text = input("Enter the text: ")
    return text.strip()


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char = len(text.replace(" ", ""))
    return char


def count_sentences(text):
    sentence = 0
    for i in text:
        if i in ['.', '!', '?']:
            sentence += 1

    return sentence


def display_result():
    get_text()
    count_words(text)
    count_characters(text)
    count_sentences(text)
    print("")
