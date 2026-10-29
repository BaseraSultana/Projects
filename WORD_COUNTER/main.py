
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


def count_all():
    """Display word, character, and sentence counts for user-provided text."""
    text = get_text()
    words = count_words(text)
    chars = count_characters(text)
    sentences = count_sentences(text)
    result = (f"Word Count: {words} ", f"Character Count: {chars} ",
              f"Sentence Count: {sentences}")
    print("\nRESULT\n" + "\n".join(result))


def get_choice():
    choice = input("Enter Your Choice: ").strip()
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid Input. Please enter a valid number!")
    text = get_text()
    if choice == 1:
        count_words(text)
    elif choice == 2:
        count_characters(text)
    elif choice == 3:
        count_sentences(text)
    elif choice == 4:
        count_all()
    elif choice == 5:
        print("Exiting......")
        raise SystemExit
    else:
        print("Invalid Input. Enter a number between 1 to 5.")


def menu():
    print("    Welcome to Word Counter!    \n", "\nWhat do you want to count?")
    menu = ("1. COUNT WORDS", "2. COUNT CHARACTERS",
            "3. COUNT SENTENCES", "4. COUNT ALL", "5. EXIT")
    print("\n".join(menu))
    get_choice()
