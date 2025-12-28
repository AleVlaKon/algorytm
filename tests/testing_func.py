from itertools import accumulate


def min_valid_index(nums, k, m):
    total = list(accumulate(nums, initial=0))

    for i in range(len(nums) - k):
        if total[i + k + 1] - total[i] == m:
            return i

    return -1


