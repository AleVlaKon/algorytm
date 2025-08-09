def restore_values(nums):
    min_element = min(nums) // 2
    return [i - min_element for i in nums]


print(restore_values([5, 9, 4, 7, 8]))
print(restore_values([2, 3, 4, 5, 6, 7, 8, 9, 10]))