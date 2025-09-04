import sys

from stats import get_num_words
from stats import get_char_frequency
from stats import get_sorted_char_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(sort_list, num_words):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sort_list:
        char = dict["char"]
        if char.isalpha():
            num = dict["num"]
            print(f"{char}: {num}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    file_content = get_book_text(path_to_book)
    num_words = get_num_words(file_content)
    print(f"{num_words} words found in the document")
    
    char_freq = get_char_frequency(file_content)
    for char in char_freq:
        freq = char_freq[char]
        print(f" {char}, counts: {freq}")

    sort_list = get_sorted_char_list(char_freq)
    print_report(sort_list, num_words)

main()

