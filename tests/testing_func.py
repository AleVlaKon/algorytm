def find_majority_element(nums: list[int]):
    majority_element = nums[0]
    counter = 0
    for num in nums:
        if num == majority_element:
            counter += 1
        else:
            counter -= 1
        if counter == 0:
            majority_element = num
    
    if counter == 0:
        return -1
    return majority_element
