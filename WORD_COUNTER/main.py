
"""Count words, characters, and sentences in user-provided text."""


def get_text():
    """Prompt for text, or return to the menu if the user enters Q."""
    while True:
        text = input("\nEnter text (or Q to return to the menu): ").strip()
        if text.casefold() == "q":
            return None
        if not text:
            print("Text cannot be empty!")
            continue
        return text


def count_words(text):
    """Return the number of whitespace-separated words in the text."""
    words = text.split()
    return len(words)


def count_characters(text):
    """Count characters in the text, excluding and including spaces."""
    print("Do you want spaces to be included?", "\n1. Yes", "\n2. No")
    choice = input("Enter Your Choice: ").strip()
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid Input. Please enter a valid !")
    if choice == 1:
        # if i want several spaces to count as just one character, then
        # chars = len(" ",join(text.split()))
        chars = len(text)
    elif choice == 2:
        chars = len(text.replace(" ", ""))
    else:
        print("Invalid Input. Enter a number between 1 and 2.")
        return None
    return chars


def count_sentences(text):
    """Count sentence-ending punctuation marks in the text."""
    sentence = 0
    in_ending = False

    for char in text:
        # if i in ['.', '!', '?']:
        # if several punctuations are present then the sentence should be counted as one.
        if char in ".!?":
            if not in_ending:
                sentence += 1
            in_ending = True
        else:
            in_ending = False

    return sentence


def count_all():
    """Display word, character, and sentence counts for user-provided text."""
    text = get_text()
    if text is None:
        return
    words = count_words(text)
    chars = count_characters(text)
    sentences = count_sentences(text)
    result = (f"Word Count: {words} ", f"Character Count: {chars} ",
              f"Sentence Count: {sentences}")
    print("\nRESULT\n" + "\n".join(result))


def main():
    """Display the menu and handle the user's selection."""
    print("\n    Welcome to Word Counter!    \n",
          "\nWhat do you want to count?")
    menu = ("1. COUNT WORDS", "2. COUNT CHARACTERS",
            "3. COUNT SENTENCES", "4. COUNT ALL", "5. EXIT")
    print("\n".join(menu))
    choice = input("Enter Your Choice: ").strip()
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid Input. Please enter a valid number!")
        return
    if choice == 5:
        print("Exiting......")
        raise SystemExit
    if choice == 4:
        count_all()
        return
    if choice not in (1, 2, 3):
        print("Invalid Input. Enter a number from 1 to 5.")
        return
    if not choice:
        print("Choice cannot be empty!")

    text = get_text()
    if text is None:
        return
    if choice == 1:
        print(f"Word Count: {count_words(text)}")
    elif choice == 2:
        print(f"Character Count: {count_characters(text)}")
    elif choice == 3:
        print(f"Sentence Count: {count_sentences(text)}")


while True:
    main()
