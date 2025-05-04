import sys
from stats import get_num_words, count_characters, get_sorted_char_list

def get_book_text(filepath) -> str:
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
       print("Usage: python3 main.py <path-to-book>")
       sys.exit(1)
    book = get_book_text(sys.argv[1])
    num_words = get_num_words(book)
    character = count_characters(book)
    print("============ BOOKBOT ============\n")
    print("Analyzing book found at books/frankenstein.txt...\n")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in get_sorted_char_list(character):
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()
