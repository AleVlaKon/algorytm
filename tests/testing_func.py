def sort_by_digit_and_value(nums):
    len_nums = len(nums)

    for i in range(len(nums) - 1):
        min_index = i

        for j in range(i + 1, len_nums):
            if abs(nums[j]) % 10 > abs(nums[min_index]) % 10:
                min_index = j
            elif abs(nums[j]) % 10 == abs(nums[min_index]) % 10 and nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]
