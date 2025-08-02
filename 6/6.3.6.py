def min_max_diff(nums: list[int]):
    max_element = float('-inf')
    min_element = float('inf')

    for i in nums:
        if i > max_element:
            max_element = i
        if i < min_element:
            min_element = i
    
    return max_element, min_element


def can_nest(nums1: list[int], nums2: list[int]) -> bool:
    max_a, min_a = min_max_diff(nums1)
    max_b, min_b = min_max_diff(nums2)

    if min_a > min_b and max_a < max_b:
        return True
    if min_b > min_a and max_b < max_a:
        return True
    return False