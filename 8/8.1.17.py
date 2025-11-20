def sort_by_digit_and_value(nums):
    len_nums = len(nums)

    for i in range(len(nums) - 1):
        min_index = i

        for j in range(i + 1, len_nums):
            if abs(nums[j]) % 10 > abs(nums[min_index]) % 10:
                min_index = j
            elif nums[j] % 10 == nums[min_index] % 10 and nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]

nums = [5, 11, 183, 19, 274]
sort_by_digit_and_value(nums)
print(nums)

nums = [5, 11, 185, 19, 271]
sort_by_digit_and_value(nums)
print(nums)

nums = [1]
sort_by_digit_and_value(nums)
print(nums)

nums = [11111, 1111, 111, 11, 1]
sort_by_digit_and_value(nums)
print(nums)