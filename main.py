def main():
    file = "books/frankenstein.txt"
    contents = get_file_contents(file)
    word_count = get_word_count(contents)
    letter_count = get_letter_count(contents)
    print(f"There are {word_count} words in this document.")
    print(f"Letter count: {letter_count}")
    

def get_file_contents(file):
    with open(file) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_letter_count(text):
    letter_count = {}
    for letter in text:
        lower_letter = letter.lower()
        try:
            old_count = letter_count[lower_letter]
            letter_count[lower_letter] = old_count + 1
        except KeyError:
            letter_count[lower_letter] = 1

    return letter_count


main()
