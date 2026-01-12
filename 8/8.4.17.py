def sort_binary_list(nums):
    counts = [0, 0]

    for element in nums:
        counts[element] += 1

    index = 0

    for num in (0, 1):
        for _ in range(counts[num]):
            nums[index] = num
            index += 1


    return counts

binary_list = [0, 1]
sort_binary_list(binary_list)
print(binary_list)