def steps_to_max(nums: list[int]) -> int:
    max_element = nums[0]
    count = 1
    result = 0
    for i in range(1, len(nums)):
        diff = abs(max_element - nums[i])
        if nums[i] > max_element:
            max_element = nums[i]
            result += diff * count
        else:
            result += diff
        count += 1

    return result



print(steps_to_max([2, 3, 4]))    # 2 -> 3 -> 4; 3 -> 4

print(steps_to_max([3, 2, 3]))    # 2 -> 3
print(steps_to_max([3, 3, 3]))    # 0
print(steps_to_max([-1, -2, -3]))    # -2 -> -1; -3 -> -2 -> -1
