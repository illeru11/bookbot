from stats import count_words, count_char

def get_book(path_to_file):
    #Pulls in a string from a file
    with open(path_to_file) as f:
        file_string = f.read()
    return file_string


def count_char(text):
    #Counts the number of characters in a string
    if text is None:
        return 0
    small_text = text.lower()
    small = list(small_text)

    #alphabet_string = "abcdefghijklmnopqrstuvwxyz"
    #alphabet = list(alphabet_string)
    
    count_list = {}
    alphabet = []
    #set values of the first dictionary
    #for char in range(0,len(alphabet)+1):
        #count_list ={char: 0}
    
    for s in small:
        if s in count_list:
            count_list[s] += 1   
        else:
            count_list[s] = 1 

    return count_list

    

    
    #text.split
    
    #return len(text)

def main():
    book = "books/frankenstein.txt"
       
    text = get_book(book)
    w_count = count_words(text)
    #expected_result = 75767
    print(f"{w_count} words found in the document")
    c_count =count_char(text)
    print(f"{c_count}")



#end

    #value = count_char(text)
    #print (value)
main()  