def shortest_sublist_with_greater_sum(nums, k):
    left = 0
    right = 0
    subspisok_lengh = float('inf')
    cur_sum = nums[0]
    n = len(nums)

    if len(nums) == 1 and nums[0] > k:
        return 1

    while right < n:
        srez = nums[left:right + 1]
        if cur_sum <= k:
            cur_sum += nums[right + 1]
            right += 1
        else:
            current_lengh = right - left
            subspisok_lengh = min(subspisok_lengh, current_lengh)
            cur_sum -= nums[left]
            left += 1

    return subspisok_lengh + 1 if subspisok_lengh != float('inf') else -1


# print(shortest_sublist_with_greater_sum([1, 3, 4, 2, 1, 5, 1], 9))
# print(shortest_sublist_with_greater_sum([1, 3, 4, 2, 1, 5, 1], 11))  
# print(shortest_sublist_with_greater_sum([1, 3, 4, 2, 1, 5, 1], 20))
# print(shortest_sublist_with_greater_sum([5], 1))
print(shortest_sublist_with_greater_sum([3, 3, 3, 3], 11))