def find_sum_indexes(nums: list[int], value: int) -> tuple[int, int]:
    for start in range(len(nums)):
        summa = 0
        for end in range(start, len(nums)):
            summa += nums[end]
            if summa == value:
                return start, end
            if summa > value:
                break
    return -1


print(find_sum_indexes([1, 2, 3, 4, 5, 6], 10))        # подсписок [1, 2, 3, 4]
print(find_sum_indexes([1, 5, 1, 2, 4, 7, 6], 7))      # подсписок [1, 5, 1]
print(find_sum_indexes([8, 7, 3, 4, 5, 33, 14], 7))    # подсписок [7]