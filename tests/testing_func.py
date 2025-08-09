def restore_values(nums):
    min_element = min(nums) // 2
    return [i - min_element for i in nums]