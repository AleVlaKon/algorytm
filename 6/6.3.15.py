def max_consecutive_ones(nums):
    count = 0
    max_count = 0
    for i in range(len(nums)):
        if nums[i]:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0

    return max_count


print(max_consecutive_ones([1, 1, 0, 1, 1, 1]))
print(max_consecutive_ones([1, 0, 1, 1, 0, 1]))
print(max_consecutive_ones([1, 1, 1, 1, 1, 1]))
print(max_consecutive_ones([0, 0, 0, 0]))
print(max_consecutive_ones([1]))
print(max_consecutive_ones([1, 0]))