def get_book(path_to_file):
    #Pulls in a string from a file
    with open(path_to_file) as f:
        file_string = f.read()
        #print(f"Text length: {len(file_string)} characters")
        #print(f"First 100 characters: {file_string[:100]}")
        
        return file_string
def count_words(text):
    #Counts the number of words in a string
    if text is None:
        return 0
    words = text.split()
    return len(words)

def main():
    book = "books/frankenstein.txt"
       
    text = get_book(book)
    w_count = count_words(text)
    #expected_result = 75767
    print(f"{w_count} words found in the document")
main()