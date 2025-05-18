def letter_by_sum(letters: list):
    alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    sum_letters = sum([alphabet[i] for i in letters])
    asxii_letters = 'abcdefghijklmnopqrstuvwxyz'
    return asxii_letters[sum_letters % 26 - 1]

print(letter_by_sum(['a', 'b']))              # 1 + 2 = 3
print(letter_by_sum(['a', 'z']))              # 1 + 26 = 27
print(letter_by_sum(['z', 'z']))              # 26 + 26 = 52
