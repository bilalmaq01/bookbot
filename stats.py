def get_word_count(filepath):
    with open(filepath) as f:
        content = f.read()
    list_of_words = content.split()
    return len(list_of_words)
def get_letter_count(filepath):
    letters = {}
    with open(filepath) as f:
        content = f.read()
    list_of_words = content.split()
    for word in list_of_words:
        for letter in word:
            if letter.lower() in letters:
                letters[letter.lower()] += 1
            else:
                letters[letter.lower()] = 1
    return letters


