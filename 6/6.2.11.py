def find_majority_element(nums: list[int]):
    majority_element = nums[0]
    counter = 0
    for num in nums:
        if counter == 0:
            majority_element = num

        if num == majority_element:
            counter += 1
        else:
            counter -= 1

    
    if nums.count(majority_element) > len(nums) // 2:
        return majority_element
    return -1



print(find_majority_element([1, 1, 1, 2, 2])) #1
print(find_majority_element([1, 1, 1, 2, 2, 2, 2, 2])) #2
print(find_majority_element([3])) #3
print(find_majority_element([1, 2, 3, 2, 2])) #2
print(find_majority_element([1, 2])) #-1
print(find_majority_element([1, 2, 3, 2])) #-1
data = list(range(10 ** 5))
print(find_majority_element(data))
data = list(range(1001))
print(find_majority_element(data))
