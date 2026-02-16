def max_average_sublist(nums, k):
    left = 1
    right = k
    max_avg = 0
    cur_avg = 0

    for i in range(k):
        max_avg += nums[i]
        cur_avg += nums[i]

    while right < len(nums):
        cur_avg = cur_avg + nums[right] - nums[left - 1]
        max_avg = max(max_avg, cur_avg)
        left += 1
        right += 1

    return max_avg / k

# print(max_average_sublist([2, 1, 5, 3, 1, 4], 3))    # (1 + 5 + 3) / 3 = 3-3.0]
# print(max_average_sublist([2, 1, 5, 3, 1, 4], 3))    # (1 + 5 + 3) / 3 = 3
# print(max_average_sublist([4, -1, 3, -2, 7, 5], 4))  # (3 - 2 + 7 + 5) / 4 = 3.25
# print(max_average_sublist([-3, -5, -2, -3, -4], 2))  # (-5 - 2) / 2 = -2.5', expected = '-2.5'
# print(max_average_sublist([0, -1], 2)) #', expected = '-0.5'
# print(max_average_sublist([-1, 0, 1], 3))            # (-1 + 0 + 1) / 3 = 0.0
# print(max_average_sublist([-3, -5, -2, -3, -4], 2))  # (-2 - 3) / 2 = -2.5
# print(max_average_sublist([5], 1))                   # 5 / 1 = 5.0
# print(max_average_sublist([4, -1, 3, -2, 7, 5], 4))  # (3 - 2 + 7 + 5) / 4 = 3.25