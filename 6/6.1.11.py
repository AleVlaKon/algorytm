def linear_search(nums: list[int], target: int, reverse: bool=False) -> int:
    if reverse:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == target:
                return i
    else:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
    return -1


print(linear_search([1, 5, 7], 5))
print(linear_search([2, 1, 7, 2], 2))
print(linear_search([12, 4, 1], 9))