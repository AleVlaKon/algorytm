def upper_bound(nums, target):
    left, right = 0, len(nums) - 1
    potential_index = -1
    while left <= right:
        middle = (right + left) // 2
        elem = nums[middle]
        if elem == target:
            potential_index = middle
            left = middle + 1
        elif elem > target:
            right = middle - 1
        elif elem < target:
            left = middle + 1
    return potential_index


print(upper_bound([1, 1, 2, 4, 4, 4, 5, 5], 0))
print(upper_bound([1], 1))

print(upper_bound([1, 1, 2, 2, 4, 4, 5, 5], 2))
print(upper_bound([1, 1, 2, 4, 4, 4, 5, 5], 3))