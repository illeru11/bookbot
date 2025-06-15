def count_words(text):
    #Counts the number of words in a string
    if text is None:
        return 0
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def count_char(text):
    #Counts the number of characters in a string
    if text is None:
        return 0
    small_text = text.lower()
    small = list(small_text)
    
    
    #for s in small:
        #if s in count_list:
           # dict_[char: s, "num"]
            #count_list[s] += 1   
       # else:
         ##   dict_append = {"char": s, "num": 1}
        #    count_list.append(dict_append)

    #return count_list

    count = {}
    for s in small:
        if s in count:
            count[s]+= 1
        else:
            count[s] = 1
    
    count_list = []
    for char, num  in count.items():
        count_list.append({"char":char,"num":num})
    count_list.sort(reverse=True,key=sort_on)


    #update_dict = {}
    #for u in update_dict in count_list:
       # if u in updated_dict:
            #pass
        #else:
          #  updated_dict[a]
    
    return count_list