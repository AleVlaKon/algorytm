def get_max_prefix_sum(nums):
    cur_sum = nums[0]
    max_sum = nums[0]
    for i in range(1, len(nums)):
        cur_sum += nums[i]
        max_sum = max(max_sum, cur_sum)
    return max_sum




print(get_max_prefix_sum(([2, 4, 1, 3])))      # префикс с наибольшей суммой: [2, 4, 1, 3]
print(get_max_prefix_sum(([2, 4, -1, -3])))    # префикс с наибольшей суммой: [2, 4]
print(get_max_prefix_sum(([-2, 4, 1, -3])))    # префикс с наибольшей суммой: [-2, 4, 1]
print(get_max_prefix_sum(([-2, -4, -1, -3])))  # префикс с наибольшей суммой: [-2]



