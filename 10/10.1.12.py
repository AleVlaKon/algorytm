from itertools import accumulate


def min_valid_index(nums, k, m):
    total = list(accumulate(nums, initial=0))

    for i in range(len(nums) - k):
        if total[i + k + 1] - total[i] == m:
            return i

    return -1



print(min_valid_index([7, 2, 3, 1, 4, 1, 1], 2, 6))    # [2, 3, 1]
print(min_valid_index([7, 3, 1, 4, 1, 1], 1, 5))       # [1, 4]
print(min_valid_index([7, 3, 1, 4, 1, 1], 3, 20))
print(min_valid_index([1, 1, 3, 2, 5, 9, -2], 1, 7))   # [2, 5]
