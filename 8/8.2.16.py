def number_of_swaps(nums):
    n = len(nums)
    count = 0

    for i in range(n -1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                count += 1
    return count


print(number_of_swaps([1, 2, 3, 4, 5]))