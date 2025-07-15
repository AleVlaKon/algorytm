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

    if odds == 0 or evens == 0:
        result = True
    if len_nums % 2 == 1 and abs(odds - evens) == 1:
        result = True

    elif len_nums % 2 == 0 and abs(odds - evens) == 0:
        result = True

    return result










print(adjacent_parity([5, 2, 2, 7, 1]))  # 5, 2, 7, 2, 1 True
print(adjacent_parity([1, 3, 2, 5])) # False
print(adjacent_parity([1, 1, 1, 1, 1]))        # 1, 1, 1, 1, 1 True
print(adjacent_parity([8, 2, 1, 3, 10, 9]))    # 8, 1, 2, 3, 10, 9
print(adjacent_parity([1, 3, 5, 7, 2, 4, 6]))  # 1, 2, 3, 4, 5, 6, 7

