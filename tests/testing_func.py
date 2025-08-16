from operator import lt, gt


def binary_search(nums, target):
    if nums[-1] > nums[0]:
        _func = lt
    else:
        _func = gt

    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        elem = nums[middle]
        if elem == target:
            return middle
        if _func(elem, target):
            left = middle + 1
        else:
            right = middle - 1
    return -1