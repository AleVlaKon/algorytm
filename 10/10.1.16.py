def difference_list(nums):
    n = len(nums)
    list_left = [0] * (len(nums) + 1)

    for i in range(1, n + 1):
        list_left[i] = list_left[i - 1] + nums[i - 1]


    sum_left = [nums[i] * i - list_left[i] for i in range(len(nums))]
    sum_right = []

    for i in range(len(nums)):
        sum_right.append(list_left[-1] - list_left[i + 1] - nums[i] * (n - i - 1))

    result = [sum_left[i] + sum_right[i] for i in range(n)]
    return result


print(difference_list([1, 4, 6]))
print(difference_list([1, 2]))
print(difference_list([1, 1, 1, 1]))
print(difference_list([10, 20, 30]))
print(difference_list([1, 2, 3, 4, 5]))
print(difference_list([1, 1, 2, 2, 3, 3]))