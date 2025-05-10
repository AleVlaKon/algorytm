def avg_values(nums: list):
    list_of_avg_values = []
    sum_i_values = 0
    for i in range(len(nums)):
        sum_i_values += nums[i]
        list_of_avg_values.append(sum_i_values / (i + 1))
    return list_of_avg_values


print(avg_values([10, 20, 30, 40, 50]))
print(avg_values([1, 1, 1, 1, 1]))
print(avg_values([-2, -3, 5, 5]))
print(avg_values([]))
print(avg_values([0, 0, 0, 0]))
