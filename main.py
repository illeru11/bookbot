from stats import count_words, count_char

def get_book(path_to_file):
    #Pulls in a string from a file
    with open(path_to_file) as f:
        file_string = f.read()
    return file_string


def pretty_report(directory,w_count, c_count):
    #Looking report of the stats
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {directory}...")
    print("----------- Word Count ----------")
    print(f"Found {w_count} total words")
    print("--------- Character Count -------")
#loop for the book output

    for c in c_count:   
        char = c["char"]
        num = c["num"]
        print(f"{char}: {num}")
    
    print("============= END ===============")

def main():
    book = "books/frankenstein.txt"
       
    text = get_book(book)
    w_count = count_words(text)
    #expected_result = 75767
    print(f"{w_count} words found in the document")
    c_count =count_char(text)
    #print(f"{c_count}")
    pretty_report(book, w_count, c_count) 



main()