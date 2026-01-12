def move_zeros(nums: list[int]):
    k = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1
        
    while k < len(nums):
        nums[k] = 0
        k += 1
    



nums = [0, 2, 0, 0, 1]
move_zeros(nums)
print(nums)

