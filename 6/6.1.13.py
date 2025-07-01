def search_insert_position(nums: list[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        if nums[i] > target:
            return i
    return len(nums)

print(search_insert_position([1, 2, 3, 4, 5], 5))
print(search_insert_position([1, 2, 3, 4, 5], 6))
print(search_insert_position([1, 2, 4, 5], 3))