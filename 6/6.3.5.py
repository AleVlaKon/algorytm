def min_max_diff(nums: list[int]):
    max_element = float('-inf')
    min_element = float('inf')

    for i in nums:
        if i > max_element:
            max_element = i
        if i < min_element:
            min_element = i
    
    return max_element - min_element


print(min_max_diff([4, 5, 3, 2, 1]))      # 5 - 1 = 4