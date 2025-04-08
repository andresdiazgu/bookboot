import sys

def get_book_text(file_path):
    with open(file_path) as book:
        file_contents = book.read()
    return file_contents

from stats import num_words, letters_count, sort_chars

def main ():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = get_book_text(file_path)
    word_count = num_words(text)
    char_counts = letters_count(text)
    sorted_chars = sort_chars(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_info in sorted_chars:
        char = char_info["char"]
        count = char_info["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()
