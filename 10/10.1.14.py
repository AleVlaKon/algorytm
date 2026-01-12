def zeros_in_segments(nums, segments):
    list_zeros = [0] * (len(nums) + 1)

    count_zeros = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count_zeros += 1
        list_zeros[i + 1] = count_zeros

    result = [list_zeros[r + 1] - list_zeros[l] for l, r in segments]

    return result

print(zeros_in_segments([0], [(0, 0)]))