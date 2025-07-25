from itertools import groupby


def max_consecutive_ones(nums):
    groups = groupby(nums)
    result = 0
    for key, value in groups:
        sum_values = sum(value)
        if key == 1 and sum_values > result:
            result = sum_values

    return result


print(max_consecutive_ones([1, 1, 0, 1, 1, 1]))
print(max_consecutive_ones([1, 0, 1, 1, 0, 1]))
print(max_consecutive_ones([1, 1, 1, 1, 1, 1]))
print(max_consecutive_ones([0, 0, 0, 0]))
print(max_consecutive_ones([1]))
print(max_consecutive_ones([1, 0]))