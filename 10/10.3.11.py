def could_type(word, typed):
    left_word = 0
    left_typed = 0


    while left_typed < len(typed) - 1:
        if word[left_word] == typed[left_typed] and word[left_word] == typed[left_typed + 1]:
            left_typed += 1
        elif word[left_word] == typed[left_typed] and word[left_word] != typed[left_typed + 1]:
            left_typed += 1
            left_word += 1
        else:
            return False
    return True



print(could_type('beegeek', 'geekbee'))
print(could_type('python', 'pyytttthonnn'))


