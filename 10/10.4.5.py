def has_duplicates_within_range(nums, k):
    left = 0
    right = k
    diapazon = set(nums[:k])
    # print(left, right, diapazon)
    n = len(nums)

    if len(diapazon) < len(nums[:k]):
        return True

    while right < n:
        left_elem = nums[left]
        right_elem = nums[right]
        if right_elem in diapazon:
            return True
        else:
            diapazon.add(right_elem)
            diapazon.remove(left_elem)
            left += 1
            right += 1
    
    return False


# print(has_duplicates_within_range([3, 1, 5, -4, 5, 2], 3))    # дубликаты: 5
print(has_duplicates_within_range([1, 1, 5, -4, 2, 5], 3))    # дубликаты: 1, 5
print(has_duplicates_within_range([5, 1, 3, -4, 2, 5], 3))    # дубликатов нет
print(has_duplicates_within_range([-2, -1, -2, -1], 2))       # дубликаты: -2, -1