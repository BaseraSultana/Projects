
"""Count words, characters, and sentences in user-provided text."""


def get_text():
    """prompt the user to enter the text"""
    text = input("\nEnter the text (or) enter 'Q' to Exit : ")
    if text.casefold() == "q":
        print("Exiting......")
        main()
    if not text:
        print("Text cannot be empty!")
        get_text()
    return text.strip()


def count_words(text):
    """Return the number of whitespace-separated words in the text."""
    words = text.split()
    return len(words)


def count_characters(text):
    """Count characters in the text, excluding spaces."""
    print("Do you want spaces to be included?", "\n1. Yes", "\n2. No")
    choice = input("Enter Your Choice: ").strip()
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid Input. Please enter a valid number!")
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
    for index, in text:
        # if i in ['.', '!', '?']:
        #     if i+1 in ['.', '!', '?']:

        sentence += 1
    return sentence


def count_all():
    """Display word, character, and sentence counts for user-provided text."""
    text = get_text()
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
        print("Invalid Input. Enter a number from 1 to 5.")
        return None


while True:
    main()
