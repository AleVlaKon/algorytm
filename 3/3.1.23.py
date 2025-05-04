def optimal_value(nums: list[int]):
    a = len(nums)
    b = -2 * sum(nums)
    return (-b / (2 * a))


print(optimal_value([1, 2, 9, 2, 6]))
print(optimal_value([1, 2, 3, 4, 5]))