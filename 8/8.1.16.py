def sum_of_seven_smallest(nums: list) -> None:
    len_nums = len(nums)

    for i in range(7):
        min_index = i

        for j in range(i + 1, len_nums):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]
    sum_of_seven = sum(nums[:7])

    return sum_of_seven

print(sum_of_seven_smallest([-7, -2, -2, -8, -1, -4, -10]))