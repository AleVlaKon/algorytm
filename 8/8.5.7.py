def are_anagram(s1: str, s2:str) -> bool:
    return ''.join(sorted(s1)) ==  ''.join(sorted(s2))



print(are_anagram('listen', 'silent'))
print(are_anagram('race', 'care'))

print(are_anagram('dad', 'bad'))
print(are_anagram('bee', 'geek'))