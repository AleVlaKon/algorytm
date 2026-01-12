from collections import Counter

def is_subset(s1, s2):
    counts1 = Counter(s1)                         # быстрое создание и заполнение вспомогательного словаря
    counts2 = Counter(s2)                         # быстрое создание и заполнение вспомогательного словаря
    
    return counts1 <= counts2


print(is_subset('ace', 'abcde'))

print(is_subset('ace', 'abcd'))
print(is_subset('ace', 'aabbccddee'))
print(is_subset('abab', 'ab'))

