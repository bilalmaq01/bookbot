def numofwords(stringofbook):
    words = stringofbook.split()
    totalnumofwords = len(words)
    return totalnumofwords

def numofletters(text):
    lowertext = text.lower()
    chars = {}
    for char in lowertext:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sortnums(dict):
    listofnums = list(dict.items())
    listofnums.sort(key=lambda tup: tup[1], reverse=True)
    return listofnums





    
