def negatives_count_in_every_sublist(nums, k):
    left = 1
    right = k
    res = []
    count = 0

    for i in range(k):
        if nums[i] < 0:
            count += 1
    
    res.append(count)
    
    while right <= len(nums) - 1:
        left_prev = nums[left - 1]
        cur_right = nums[right]
        if left_prev < 0 and cur_right > 0:
            count -= 1
        elif left_prev > 0 and cur_right  < 0:
            count -= 1
        left += 1
        right += 1
        res.append(count)

    return res



print(negatives_count_in_every_sublist([2, -1, -3, 4, 1, 1, -4], 3)) #[2, 2, 1, 0, 1]