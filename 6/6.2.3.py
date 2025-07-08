def kth_occurrence(nums: list[int], target: int, k: int):
    k_target = 0
    for i in range(len(nums)):
        if nums[i] == target:
            k_target += 1
        if k_target == k:
            return i
    return -1


print(kth_occurrence([1, 2, 3, 1, 2, 3, 1, 2, 3, 1], 3, 3))
print(kth_occurrence([2, 2, 2, 2, 2], 2, 6))   
print(kth_occurrence([5], 5, 1))               