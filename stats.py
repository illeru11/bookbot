def count_words(text):
    #Counts the number of words in a string
    if text is None:
        return 0
    words = text.split()
    return len(words)

def count_char(text):
    #Counts the number of characters in a string
    if text is None:
        return 0
    text.lower()
    alphabetstring = "abcdefghijklmnopqrstuvwxyz"
    Count_Dictionary=alphabetstring.split()
    for char in Count_Dictionary:
        print(f" {Count_Dictionary[char]}")
    text.split
    
    #return len(text)