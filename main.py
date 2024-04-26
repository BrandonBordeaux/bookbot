def main():
    file = "books/frankenstein.txt"
    contents = get_file_contents(file)
    word_count = get_word_count(contents)
    char_count = get_char_count(contents)
    list_of_chars = convert_letter_dict(char_count)
    list_of_chars.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {file} ---")
    print(f"{word_count} words in this document\n")
    for char in list_of_chars:
        print(f"The {char["char"]} character was found {char["count"]} times")
    print("--- End report ---")
    

def get_file_contents(file):
    with open(file) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    char_count = {}
    for char in text:
        lowered = char.lower()
        try:
            old_count = char_count[lowered]
            char_count[lowered] = old_count + 1
        except KeyError:
            char_count[lowered] = 1

    return char_count


def convert_letter_dict(dict):
    letter_list = []
    for key, value in dict.items():
        if key.isalpha():
            char_dict = {
                "char": key,
                "count": value
            }
            letter_list.append(char_dict)

    return letter_list


def sort_on(dict):
    return dict["count"]


main()
