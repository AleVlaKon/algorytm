def get_closest_element(nums, target):
    left, right = 0, len(nums) - 1
    min_elem = None
    while left <= right:
        middle = (right + left) // 2
        elem = nums[middle]
        if min_elem == None:
            min_elem = elem
        else:
            min_diff = abs(elem - target)
            elem_diff = abs(min_elem - target)
            if elem_diff < min_diff:
                min_elem = elem
            elif min_diff == elem_diff and elem > min_elem:
                min_elem = elem
            

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
