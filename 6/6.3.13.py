def find_index_of_max(nums, reverse=False):
    max_element = float('-inf')
    first_index = 0
    last_index = 0
    for i in range(len(nums)):
        if nums[i] > max_element:
            max_element = nums[i]
            first_index = i
            last_index = i
        if nums[i] == max_element:
            last_index = i
    
    return last_index if reverse else first_index


print(find_index_of_max([1, 5, 3, 2, 4]))
print(find_index_of_max([3, 2, 4, 1, 4]))
print(find_index_of_max([3, 2, 4, 1, 4], reverse=True))