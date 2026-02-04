def duplicate_zeros(nums: list[int]) -> None:
    res = []

    left = 0
    count = 0

    while count < len(nums):
        if nums[left] != 0:
            res.append(nums[left])
            left += 1
            count += 1
        else:
            if nums[left] == 0:
                res.append(0)
                left += 1
            if left < len(nums):
                res.append(0)
            count += 2
                


    for i in range(len(nums)):
        nums[i] = res[i]
    


nums = [3, 0, 2, 7, 0, 1, 4, 5]
duplicate_zeros(nums)
print(nums)
        
    
