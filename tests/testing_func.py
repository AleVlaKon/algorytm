from operator import lt, gt

def alter_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        key_index = i

        condition = gt if key_index % 2 == 0 else lt
        for j in range(i + 1, n):
            if condition(nums[j], nums[key_index]):
                key_index = j
        nums[i], nums[key_index] = nums[key_index], nums[i]