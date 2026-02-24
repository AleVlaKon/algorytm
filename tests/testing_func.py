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