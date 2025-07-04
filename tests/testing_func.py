def doubling_the_value(nums: list[int], value: int) -> int:
    for i in nums:
        if i == value:
            value *= 2
    return value