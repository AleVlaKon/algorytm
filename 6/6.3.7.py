
def max_to_min(nums):
    max_element = float('-inf')
    min_element = float('inf')

    for i in range(len(nums)):
        if nums[i] > max_element:
            max_element = nums[i]
        if nums[i] < min_element:
            min_element = nums[i]
    
    for i in range(len(nums)):
        if nums[i] == max_element:
            nums[i] = min_element


data = [1, 2, 1, 2, 1, 2]
max_to_min(data)
print(data)