def is_almost_palindrome(s: str):
    data = list(s)
    counter = 0
    left = 0
    right = len(s) - 1

    while left < right:
        if data[left] == data[right]:
            left += 1
            right -= 1
        elif data[left] == data[right - 1]:
            right -= 1
            counter += 1
        elif data[right] == data[left + 1]:
            left += 1
            counter += 1
        else:
            return False

        # if counter > 1:
        #     return False
    
    return counter == 1

print(is_almost_palindrome('abca'))
print(is_almost_palindrome('abcddba'))    # abddba
print(is_almost_palindrome('spyder'))