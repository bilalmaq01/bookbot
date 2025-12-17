from stats import get_word_count,get_letter_count,formatted
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content
def main():
    text = get_book_text("books/frankenstein.txt")
    wordcount = get_word_count("books/frankenstein.txt")
    letter_count = get_letter_count("books/frankenstein.txt")
    sorted_list = formatted(letter_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        ch = char["char"]
        if ch.isalpha():
                print(f"{ch}: {char["num"]}")
    print(sys.argv[0])
main()

