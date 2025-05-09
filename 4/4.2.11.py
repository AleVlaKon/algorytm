def longest_substring_without_vowels(s: str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    max_count = 0
    for letter in s:
        if letter in vowels:
            count = 0
        else:
            count += 1
            if count > max_count:
                max_count = count
    return max_count


print(longest_substring_without_vowels('abcdefg'))       # bcd
print(longest_substring_without_vowels('bcdgf'))         # bcdgf

print(longest_substring_without_vowels('aeiou'))         # согласных букв нет
print(longest_substring_without_vowels('abecidofug'))    # b, c, d, f, g
print(longest_substring_without_vowels('x'))             # x
print(longest_substring_without_vowels('abbbabbaba'))    # bbb