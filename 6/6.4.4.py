def get_closest_element(nums: list[int], target: int) -> int:
    min_difference = abs(nums[0] - target)
    result = nums[0]
    for i in range(1, len(nums)):
        if abs(nums[i] - target) < min_difference:
            result = nums[i]
            min_difference = abs(nums[i] - target)
        if abs(nums[i] - target) == min_difference and nums[i] > result:
            result = nums[i]

    return result


print(get_closest_element([1, 2, 3, 4], 5))
print(get_closest_element([1, -1, 3], 0))
print(get_closest_element([1], 5))
print(get_closest_element([5, 4, 3, 2, 1], 3))
print(get_closest_element([1, 1, 1, 1, 1, 1], 2))
