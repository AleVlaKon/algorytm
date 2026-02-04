def duplicate_zeros(nums: list[int]) -> None:
    res = []

    left = 0
    while left < len(nums):
        if nums[left] == 0:
            res.append(0)
        res.append(nums[left])
        left += 1

    nums[:] = res[:len(nums)]


nums = [3, 0, 2, 7, 0, 1, 4, 5]
duplicate_zeros(nums)
print(nums)
        
    
