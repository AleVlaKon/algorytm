def return_max_min_element(nums: list[int]):
    max_element = float('-inf')
    min_element = float('inf')

    for i in nums:
        if i > max_element:
            max_element = i
        if i < min_element:
            min_element = i
    
    return max_element, min_element


def find_not_min_max(nums):
    max_element, min_element = return_max_min_element(nums)
    for num in nums:
        if num != max_element and num != min_element:
            return num
        
print(find_not_min_max([1, 2, 3]))
print(find_not_min_max([2, 3, 4, 1, 5]))
print(find_not_min_max([5, 4, 3, 2, 1]))
print(find_not_min_max([3, 6, 2, 1]))
print(find_not_min_max([7, 10, 1, 2]))