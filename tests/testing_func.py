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