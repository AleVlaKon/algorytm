def bounded_binary_search(nums, target, left=0, right=None):
    if right == None:
        right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        elem = nums[middle]
        if elem == target:
            return middle
        if elem < target:
            left = middle + 1
        if elem > target:
            right = middle - 1
    return -1


print(bounded_binary_search([1], 1,left=0))