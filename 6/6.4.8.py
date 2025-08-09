def max_sum(nums):
    result = -1 
    current_result = -1
    flag = False
    for num in nums:
        if num < 0:
            result = max(result, current_result)
            current_result = 0
            flag = True
        elif flag:
            current_result += num
    return result

print(max_sum([1, -2, -3, 4]))
print(max_sum([1, -2, 3, 4, -5]))
print(max_sum([-1, 2, 3, -5, 6, 7, -8]))
print(max_sum([1, 2, -3, 4, 5]))
print(max_sum([1, 2, 3, 4, 5]))    
print(max_sum([-1, -2]))     