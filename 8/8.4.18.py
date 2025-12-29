def sort_limited_numbers(nums):
    min_value, max_value = min(nums), max(nums)
    counts = [0] * (max_value - min_value + 1)

    for elem in nums:
        counts[elem - min_value] += 1

    index = 0

    for num in range(max_value - min_value + 1):
        for _ in range(counts[num]):
            nums[index] = num + min_value
            index += 1

nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
sort_limited_numbers(nums)
print(nums)

nums = [-15, 10, 1, -8, 24]
sort_limited_numbers(nums)
print(nums)