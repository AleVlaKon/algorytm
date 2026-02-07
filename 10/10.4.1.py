def smallest_palindrome(s: str) -> str:
    left = 0
    right = len(s) - 1
    data = list(s)

    while left < right:
        if data[left] != data[right]:
            if data[left] < data[right]:
                data[right] = data[left]
            else:
                data[left] = data[right]
        left += 1
        right -= 1

    return ''.join(data)


print(smallest_palindrome('beegeek'))
print(smallest_palindrome('pygen'))
print(smallest_palindrome('abcd'))