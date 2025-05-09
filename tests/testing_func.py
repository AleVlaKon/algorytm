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