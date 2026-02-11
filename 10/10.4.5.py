def pair_with_lower_or_equal_difference(nums, k):
    left = 0
    right = 0
    diff = float('inf')
    curr_min_elem = nums[0]
    curr_max_elem = nums[0]
    min_elem = float('inf')
    max_elem = 0

    while right < len(nums) - 1:
        if nums[right] - nums[left] <= k and right < len(nums) - 1:
            right += 1
            curr_max_elem = nums[right]
        else:
            while nums[right] - nums[left] > k:
                left += 1
                curr_min_elem = nums[left]
            if max_elem - min_elem <= k and max_elem - min_elem > :
                min_elem = curr_min_elem
                max_elem = curr_max_elem

    return min_elem, max_elem


print(pair_with_lower_or_equal_difference([2, 4, 7, 8, 10, 11], 3))