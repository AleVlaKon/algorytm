def alternate_order(nums: list[int]) -> list[int]:
    left = 1
    res = [nums[0]]

    while left <= len(nums) // 2:
        res.extend([nums[-left], nums[left]])
        left += 1

    if not len(nums) % 2 and len(nums) != 1:
        res.pop()

    return res


print(alternate_order([1, 2, 3, 4, 5, 6]))
print(alternate_order([2, 8, 6, 0, 4]))
print(alternate_order([1]))