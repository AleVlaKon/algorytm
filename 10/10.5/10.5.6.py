def uniques_count_in_every_sublist(nums, k):
    left = 0
    right = k
    n = len(nums)
    res = []

    while right <= n:
        diapazon = set(nums[left:right])
        res.append(len(diapazon))
        left += 1
        right += 1

    return res


print(uniques_count_in_every_sublist([2, 5, 5, 5, -3, 1, -3], 3))
print(uniques_count_in_every_sublist([1, 2, 3, 4, 5], 5))
print(uniques_count_in_every_sublist([1], 1))
print(uniques_count_in_every_sublist([2, 2, 2, 2, 2], 2))
print(uniques_count_in_every_sublist([1, -1, 2, -2, 1, -1], 4))
print(uniques_count_in_every_sublist([1, 2, 1, 3, 4, 2, 3], 4))