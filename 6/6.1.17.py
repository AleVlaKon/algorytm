def doubling_the_value(nums: list[int], value: int) -> int:
    for i in nums:
        if i == value:
            value *= 2
    return value


print(doubling_the_value([1, 2, 3, 4, 8], 2))     # 2 -> 4 -> 8 -> 16
print(doubling_the_value([1, 2, 3, 4, 8], 3))     # 3 -> 6
print(doubling_the_value([1, 2, 3, 4, 8], 10))    # 10
print(doubling_the_value([1], 1))                 # 2