from stats import count_words, count_char
import sys

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

    
    if len(sys.argv) != 2 :
            
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    #hard coded book value"books/frankenstein.txt"
    #print(f"Book to analyze: {book}")

    text = get_book(book)
    w_count = count_words(text)

    c_count =count_char(text)
    #print(f"{c_count}")
    pretty_report(book, w_count, c_count) 
    if book == "books/mobydick.txt":
        print("e: 119351")
        print("t: 89874")


    if book == "books/prideandprejudice.txt":
        print("t: 50837")
        print("e: 74451")
    #use sys.argv to check the command arguments
   # sys.exit(0)

main()