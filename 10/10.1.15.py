def valid_nums_in_segments(nums, segments):
    list_zeros = [0] * (len(nums) + 1)

    count_neib = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count_neib += 1
        list_zeros[i + 1] = count_neib

    result = [list_zeros[r + 1] - list_zeros[l + 1] for l, r in segments]

    return result


print(valid_nums_in_segments([4, 8, 9, 5, 4, 3, 2, 5], [(0, 3), (2, 5), (5, 7)]))