def sort_half_sorted(nums):
    left = 0
    right1 = right2 = len(nums) // 2 + len(nums) % 2

    res = []

    while left < right2 and right1 < len(nums):
        if nums[left] < nums[right1]:
            res.append(nums[left])
            left += 1
        else:
            res.append(nums[right1])
            right1 += 1

    while left < right2:
        res.append(nums[left])
        left += 1


    while right1 < len(nums):
        res.append(nums[right1])
        right1 += 1

    return res


print(sort_half_sorted([1, 2, 3, 4, 5]))
# print(sort_half_sorted([1, 2, 3, 4]))
# print(sort_half_sorted([1, 2, 3, 4, 5]))