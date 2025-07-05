def count_occurrences(nums, target, start, end):
    count = 0
    for i in range(start, end):
        if nums[i] == target:
            count += 1
    return count

