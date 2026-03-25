def has_triplet_sum(nums):
    nums.sort()
    n = len(nums)

    for c in range(n - 1, 1, -1):
        target = nums[c]

        left = 0
        right = c - 1

        while left < right:
            cur_sum = nums[left] + nums[right]

            if cur_sum == target:
                return True

            elif cur_sum < target:
                left += 1

            else:
                right -= 1

    return False
                
print(has_triplet_sum([10, 1, 5, 2, 2]))