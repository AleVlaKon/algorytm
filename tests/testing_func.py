def lowercase_before_uppercase(s: str) -> bool:
    char_index = 0
    while s[char_index] == s[char_index].lower():
        if char_index != len(s) - 1:
            char_index += 1
        else:
            break
    for char in range(char_index+1, len(s)):
        if s[char] == s[char].lower():
            return False
    return True