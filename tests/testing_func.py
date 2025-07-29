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

