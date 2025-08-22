def get_closest_element(nums, target):
    left, right = 0, len(nums) - 1
    min_elem = None
    while left <= right:
        middle = (right + left) // 2
        elem = nums[middle]
        min_elem = min(nums[left], nums[right], key=lambda x: abs(target - x))
            

        if target < elem: 
            right = middle - 1
        else:
            left = middle + 1
    return min_elem


print(get_closest_element([1, 2, 3, 5], 4))
print(get_closest_element([1, 2, 3, 4, 5], 4))
print(get_closest_element([1, 2, 3, 4, 4], 5))
print(get_closest_element([2, 3, 4, 5], 1))
print(get_closest_element([1, 1, 2, 2, 4, 4], 3))
