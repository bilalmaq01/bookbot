from stats import get_word_count,get_letter_count,formatted
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content
def main():
    if(len(sys.argv) != 2):
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

