from stats import numofwords
from stats import numofletters
from stats import sortnums
import sys

def get_book_text(book):
    with open(book) as f:
        readbook = f.read()
    return readbook
    


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    totalnumwords = numofwords(text)
    letterdict = numofletters(text)
    sorted = sortnums(letterdict)
    print ("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {totalnumwords} total words")
    print("--------- Character Count -------")
    for char in sorted:
        if char[0].isalpha() == True:
            print(f"{char[0]}: {char[1]}")
    print("============= END ===============")


main()