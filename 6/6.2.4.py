def find_sum_indexes(nums, value):
    start = 0
    cur_sum = 0 

    for end in range(len(nums)):
        cur_sum += nums[end]
        while cur_sum > value and start <= end:
            cur_sum -= nums[start]
            start += 1        
        if cur_sum == value:
            return (start, end)

    return -1

print(find_sum_indexes([1, 2, 3, 4, 5, 6], 10))        # подсписок [1, 2, 3, 4]
print(find_sum_indexes([1, 5, 1, 2, 4, 7, 6], 7))      # подсписок [1, 5, 1]
print(find_sum_indexes([8, 7, 3, 4, 5, 33, 14], 7))    # подсписок [7]