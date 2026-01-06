def are_anagram(s1: str, s2:str) -> bool:
    return ''.join(sorted(s1)) ==  ''.join(sorted(s2))