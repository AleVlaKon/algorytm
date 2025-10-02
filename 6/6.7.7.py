def search_insert_position(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        middle = (right + left) // 2
        elem = nums[middle]
        if elem == target:
            return middle
        elif elem > target:
            right = middle - 1
        elif elem < target:
            left = middle + 1
    return right + 1


print(search_insert_position([1, 2, 3, 5, 6], 4))
print(search_insert_position([1, 2, 3, 5, 6], 0))
print(search_insert_position([1, 2, 3, 5, 6], 3))
print(search_insert_position([1, 2, 3, 5, 6], 7))
print(search_insert_position([0, 2, 4], 1))
print(search_insert_position([-9, -8, -4, -3, 1, 2, 3, 7, 8, 9], 2))