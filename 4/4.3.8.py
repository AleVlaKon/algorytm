def is_order(nums: list[int], strict=True) -> bool:
    vozr = True
    ub = True
    not_vozr = True
    not_ub = True
    for i in range(1, len(nums)):
        if nums[i-1] <= nums[i]:
            vozr = False
        if nums[i-1] >= nums[i]:
            ub = False
        if nums[i-1] < nums[i]:
            not_vozr = False
        if nums[i-1] > nums[i]:
            not_ub = False

    if strict:
        return vozr or ub
    else:
        return not_vozr or not_ub



print(is_order([1, 2, 3, 4, 5], strict=True))
print(is_order([1, 2, 2, 3, 3]))
print(is_order([1, 2, 3, 4, 5], strict=False))
print(is_order([-2, -1, 1, 2, 2, 3, 5], strict=False))
print(is_order([1, 3, 2, 4, 5], strict=False))
print(is_order([1], strict=True))