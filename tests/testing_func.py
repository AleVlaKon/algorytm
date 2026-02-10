def count_pairs_with_greater_difference(nums, k):
    left, right, count = 0, 0, 0
    n = len(nums)

    while right < n:
        if nums[right] - nums[left] > k:
            count += n - right
            left += 1
        else:
            right += 1

    return count