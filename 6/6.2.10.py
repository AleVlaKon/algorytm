from collections import Counter


def is_possible_to_split(nums: list[int]) -> bool:
    res = Counter(nums)
    res2 = res.most_common()
    if len(res2) == 1:
        return True
    if res2[0][1] == res2[1][1] and len(res) == 2:
        return True
    return False

print(is_possible_to_split([3, 3, 3, 3]))
print(is_possible_to_split([3, 2, 2, 3]))
print(is_possible_to_split([1, 2, 3, 4]))