from itertools import accumulate

def avg_values(nums: list):
    list_of_avg_values = []
    sum_i_values = 0
    for i in range(len(nums)):
        sum_i_values += nums[i]
        list_of_avg_values.append(sum_i_values / (i + 1))
    return list_of_avg_values


def avg_values(nums: list):
    list_of_avg_values = []
    for sum, i in enumerate(accumulate(nums), 1):
        list_of_avg_values.append(sum / i)
    return list_of_avg_values