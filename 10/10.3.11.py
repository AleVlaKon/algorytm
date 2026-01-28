def could_type(word, typed):
    i = 0  # указатель для word
    j = 0  # указатель для typed
    
    while j < len(typed):
        # Если дошли до конца word, то все оставшиеся символы в typed должны совпадать с последним символом word
        if i == len(word):
            if typed[j] == word[-1]:
                j += 1
            else:
                return False
        # Если символы совпадают, двигаем оба указателя
        elif word[i] == typed[j]:
            i += 1
            j += 1
        # Если символ в typed совпадает с предыдущим символом в word (и есть предыдущий символ)
        elif typed[j] == word[i - 1]:
            j += 1
        # Иначе typed нельзя получить
        else:
            return False
    
    # Проверяем, что все символы в word были использованы
    return i == len(word)


