def ternary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        block_size = (right - left) // 2
        left_middle = left + block_size
        right_middle = right - block_size
        left_elem = nums[left_middle]
        right_elem = nums[right_middle]
        if target == left_elem or target == right_elem:
            return True
        elif target < left_elem: 
            right = left_middle - 1
        elif left_elem < target < right_elem:
            left = left_middle + 1
            right = right_middle - 1
        else:
            left = right_middle + 1
    return False


print(ternary_search([1, 2, 3, 4, 5, 6, 7, 8], 6))
print(ternary_search([1, 2, 3, 4, 5, 6, 7, 8], 10))
print(ternary_search([1, 2, 3, 4, 5], 1))
print(ternary_search([-1, 0, 1], -1))
