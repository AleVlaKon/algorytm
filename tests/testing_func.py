def could_type(word, typed):
    i = 0  
    j = 0  
    
    while j < len(typed):
        if i == len(word):
            if typed[j] == word[-1]:
                j += 1
            else:
                return False
        elif word[i] == typed[j]:
            i += 1
            j += 1
        elif typed[j] == word[i - 1]:
            j += 1
        else:
            return False
    
    return i == len(word)


