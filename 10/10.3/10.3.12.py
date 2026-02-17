def is_flippable_number(num: str):
    left = 0
    right = len(num) - 1

    while left <= right:
        if num[left] == '9' and num[right] == '6':
            left += 1
            right -= 1
        elif num[right] == '9' and num[left] == '6':
            left += 1
            right -= 1
        elif num[right] == num[left] == '0':
            left += 1
            right -= 1
        else:
            return False
        
    return True




print(is_flippable_number('609'))
print(is_flippable_number('96096'))
print(is_flippable_number('6090609'))
print(is_flippable_number('6900'))
print(is_flippable_number('6'))
print(is_flippable_number('69'))