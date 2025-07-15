def adjacent_parity(nums: list[int]):
    len_nums = len(nums)
    odds = 0
    evens = 0
    result = False
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            odds += 1
        else:
            evens += 1


    if abs(odds - evens) in (0, 1, len_nums):
        result = True


    return result

