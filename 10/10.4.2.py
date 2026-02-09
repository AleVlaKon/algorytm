def has_triplet_with_zero_sum(nums: list[int]) -> bool:
    nums.sort()
    n = len(nums)

    for i in range(n):
        target = -nums[i]
        left = i + 1
        right = n - 1

        while left < right:
            sum_left_right = nums[left] + nums[right]
            if target < sum_left_right:
                right -= 1
            elif target > sum_left_right:
                left += 1
            else:
                return True

    return False


print(has_triplet_with_zero_sum([-3, -2, 4, 2, 1]))
