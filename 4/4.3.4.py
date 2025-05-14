def equilibrium(nums: list):
    if len(nums) == 1:
        return 0
    for i in range(len(nums) - 1):
        sum_left = sum(nums[:i])
        sum_right = sum(nums[i+1:])
        if sum_left == sum_right:
            return i
    if sum(nums) == nums[-1]:
        return len(nums) - 1
    return -1


print(equilibrium([1, 3, 5, 2, 2]))
print(equilibrium([1]))
print(equilibrium([1, 2]))