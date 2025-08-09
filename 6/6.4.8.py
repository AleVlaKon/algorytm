def max_sum(nums):
    result = 0
    current_result = 0
    flag = False
    check_num = False
    for i in range(len(nums)):
        if nums[i] < 0 and flag:
            if current_result > result:
                result = current_result
            current_result = 0
            check_num = True
        elif nums[i] < 0:
            flag = True
        elif nums[i] > 0 and flag:
            current_result += nums[i]
    if not check_num: 
        return -1
    return result


print(max_sum([1, -2, -3, 4]))
print(max_sum([1, -2, 3, 4, -5]))
print(max_sum([-1, 2, 3, -5, 6, 7, -8]))
print(max_sum([1, 2, -3, 4, 5]))
print(max_sum([1, 2, 3, 4, 5]))    
print(max_sum([-1, -2]))     