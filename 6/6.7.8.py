def equal(nums):
    left, right = 0, len(nums) - 1
    potential_index = -1
    while left <= right:
        middle = (right + left) // 2
        elem = nums[middle]
        if elem == middle:
            potential_index = middle
            right = middle - 1
        elif elem > middle:
            right = middle - 1
        elif elem < middle:
            left = middle + 1
    return potential_index


print(equal([-4, -2, 2, 4, 6]))
print(equal([-1, 0, 1, 2, 3, 4]))
print(equal([0]))
print(equal([0, 1, 2, 3, 4, 5]))
print(equal([-5, -4, -3, -2, -1, 0]))
print(equal([1, 2]))