import sys
from stats import get_word_count, get_letter_count, formatted

# get_book_text filepath should be a string, and return a string
def get_book_text(filepath: str) -> str:
    # open file, read-only, interpet bytes as characters
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    wordcount = get_word_count(sys.argv[1])
    letter_count = get_letter_count(sys.argv[1])
    sorted_list = formatted(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        ch = char["char"]
        if ch.isalpha():
                print(f"{ch}: {char["num"]}")
    print(sys.argv[1])
main()

