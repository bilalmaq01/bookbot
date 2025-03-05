from stats import numofwords

def get_book_text(book):
    with open(book) as f:
        readbook = f.read()
    return readbook
    


def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    totalnumwords = numofwords(text)
    print (f"{totalnumwords} words found in the document")
main()