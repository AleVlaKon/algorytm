def max_ascending_sum(nums: list[int]):
    max_sum = nums[0]
    cur_max_sum = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            cur_max_sum += nums[i]
            if cur_max_sum > max_sum:
                max_sum = cur_max_sum        
        else:
            cur_max_sum = nums[i]

    return max_sum

print(max_ascending_sum([1, 2, 3, 5, 1, 5]))
print(max_ascending_sum([1, 2, 3, 4, 5])) 
print(max_ascending_sum([10, 15, 12, 11, 8, 9, 10]))    # 10 +
print(max_ascending_sum([10, 10, 10, 10, 10])) 
print(max_ascending_sum([10]))    
print(max_ascending_sum([1, 2, 1, 2, 1, 2]))    