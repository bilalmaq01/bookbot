from stats import get_word_count,get_letter_count
def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content
def main():
    text = get_book_text("books/frankenstein.txt")
    wordcount = get_word_count("books/frankenstein.txt")
    print(f"Found {wordcount} total words")
    letter_count = get_letter_count("books/frankenstein.txt")
    print(letter_count)
main()

