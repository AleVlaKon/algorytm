def shortest_sublist_with_greater_sum(nums, k):
    left = 0
    right = 0
    subspisok_lengh = float('inf')
    cur_sum = 0
    n = len(nums)

    while right < n:
        cur_sum += nums[right]
        
        while cur_sum > k:
            subspisok_lengh = min(subspisok_lengh, right - left + 1)
            cur_sum -= nums[left]
            left += 1

        right += 1
        
    return subspisok_lengh if subspisok_lengh != float('inf') else -1


print(shortest_sublist_with_greater_sum([1, 3, 4, 2, 1, 5, 1], 9))
print(shortest_sublist_with_greater_sum([1, 3, 4, 2, 1, 5, 1], 11))  
print(shortest_sublist_with_greater_sum([1, 3, 4, 2, 1, 5, 1], 20))
print(shortest_sublist_with_greater_sum([5], 1))
print(shortest_sublist_with_greater_sum([3, 3, 3, 3], 11))