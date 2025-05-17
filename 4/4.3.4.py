def equilibrium(nums: list):
    sum_left = 0
    sum_right = sum(nums)
    for i in range(len(nums)):
        if sum_left == sum_right - sum_left - nums[i]:
            return i
        sum_left += nums[i]
    return -1


print(equilibrium([1, 3, 5, 2, 2]))
print(equilibrium([1]))
print(equilibrium([1, 2]))