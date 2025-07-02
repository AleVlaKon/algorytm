def find_number(nums):
    if nums[0] != nums[1]:
        return nums[0]
    if nums[-1] != nums[-2]:
        return nums[-1]
    for i in range(1, len(nums)):
        if  nums[i-1] < nums[i] < nums[i + 1]:
            return nums[i]


print(find_number([1, 1, 2, 3, 3]))
print(find_number([1, 1, 5, 5, 40, 60, 60]))
print(find_number([1, 1, 2, 2, 3, 3, 4]))
print(find_number([2, 10, 10]))