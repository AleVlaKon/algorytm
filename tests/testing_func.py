from collections import Counter

def is_subset(s1, s2):
    counts1 = Counter(s1)
    counts2 = Counter(s2)
    
    return counts1 <= counts2