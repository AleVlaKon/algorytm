def pair_with_lower_or_equal_difference(nums, k):
    n = len(nums)

    if n < 2:
        return None
    
    left = 0
    right = 1
    curr_diff = 0
    curr_min = nums[0]

    while right < n:
        diff = nums[right] - nums[left]
        if diff <= k and diff > curr_diff:
            min_elem = nums[left]
            max_elem = nums[right]
            curr_diff = diff
            curr_min = min_elem
        left += 1
        right += 1

    return min_elem, max_elem
            


# print(pair_with_lower_or_equal_difference([2, 4, 7, 8, 10, 11], 3))
print(pair_with_lower_or_equal_difference([2, 3, 4, 7, 8, 10, 11], 2))