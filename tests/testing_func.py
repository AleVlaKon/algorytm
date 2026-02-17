def negatives_count_in_every_sublist(nums, k):
    left = 0
    right = k
    res = []

    for i in range(right, len(nums) + 1):
        # print(nums[i - k:i])
        count = 0
        for j in range(i - k, i):
            if nums[j] < 0:
                count += 1
        res.append(count)
    return res