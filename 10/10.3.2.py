def count_pairs_with_sum(nums, k):
    left = 0
    right = len(nums) - 1
    count = 0

    while left < right:
        cur_sum = nums[left] + nums[right]
        if cur_sum == k:
            count += 1
            left += 1
            right -= 1

        elif cur_sum < k:
            left += 1

        else:
            right -= 1

    return count


print(count_pairs_with_sum([1, 1, 2, 2, 3], 4))