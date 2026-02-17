def reverse_vowels(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']

    left = 0
    right = len(s) - 1

    data = list(s)

    while left < right:
        while data[left] not in vowels:
            left += 1
        while data[right] not in vowels:
            right -= 1

        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1

    return ''.join(data)


print(reverse_vowels('programmer'))
print(reverse_vowels('crocodile'))

print(reverse_vowels('a'))
print(reverse_vowels('beegeek'))
print(reverse_vowels('aeiou'))