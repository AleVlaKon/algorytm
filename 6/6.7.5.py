def lower_bound(nums, target):
    left, right = 0, len(nums) - 1
    potential_index = -1
    while left <= right:
        middle = (right + left) // 2
        elem = nums[middle]
        if elem == target:
            potential_index = middle
            right = middle - 1
        elif elem > target:
            right = middle - 1
        elif elem < target:
            left = middle + 1
    return potential_index


print(lower_bound([10, 11, 12, 13, 14, 15], 14))
print(lower_bound([10, 11, 12, 13, 14, 15], 20))
print(lower_bound([10, 11, 12, 12, 12, 13], 12))
print(lower_bound([1, 1, 1, 1, 1], 1))
print(lower_bound([1], 1))
print(lower_bound([-1, -1, 0, 0, 1, 1], 0))