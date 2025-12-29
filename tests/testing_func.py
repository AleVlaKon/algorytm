from collections import Counter

def count_pairs(nums):
    data = Counter(nums)


    total_pairs = 0
    for count in data.values():
        total_pairs += count * (count + 1) // 2

    return total_pairs