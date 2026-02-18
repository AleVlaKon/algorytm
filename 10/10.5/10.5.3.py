def negatives_count_in_every_sublist(nums, k):
    left = 0
    right = k - 1
    res = []
    count = 0

    for i in range(k):
        if nums[i] < 0:
            count += 1
    
    res.append(count)
    
    while right < len(nums) - 1:
        cur_left = nums[left]
        cur_right = nums[right + 1]
        if cur_left < 0 and cur_right >= 0:
            count -= 1
        elif cur_left >= 0 and cur_right  < 0:
            count += 1
        left += 1
        right += 1
        res.append(count)

    return res


print(negatives_count_in_every_sublist([2, -1, -3, 4, 1, 1, -4], 3))
print(negatives_count_in_every_sublist([1, 2, 3, 4, 5], 2))
print(negatives_count_in_every_sublist([-1], 1))