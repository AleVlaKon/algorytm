def steps_to_max(nums: list[int]) -> int:
    max_element = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max_element:
            max_element = nums[i]

    result = sum(max_element - i for i in nums)
    return result





print(steps_to_max([2, 3, 4]))    # 2 -> 3 -> 4; 3 -> 4

print(steps_to_max([3, 2, 3]))    # 2 -> 3
print(steps_to_max([3, 3, 3]))    # 0
print(steps_to_max([-1, -2, -3]))    # -2 -> -1; -3 -> -2 -> -1
