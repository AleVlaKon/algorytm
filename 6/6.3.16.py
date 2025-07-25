from itertools import pairwise

def max_sum(nums):
    pairs = pairwise(nums)
    result = sum(next(pairs))
    for pair in pairs:
        result = max(result, sum(pair))

    return result


print(max_sum([1, 2, -4, -2, 3]))   # 1 + 2 + 3