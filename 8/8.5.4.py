def count_mismatches(nums):
    sorted_nums = sorted(nums)
    count = 0
    for i in range(len(nums)):
        if nums[i] != sorted_nums[i]:
            count += 1

    return count


print(count_mismatches([1, 1, 4, 2, 1, 3]))
print(count_mismatches([6, 1, 2, 3, 4, 5]))
