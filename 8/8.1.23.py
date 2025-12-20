from operator import gt, lt


def sort_by_index(nums):
    n = len(nums)
    for i in range(n - 1):
        key_index = i
        condition = gt if key_index % 2 else lt

        for j in range(i + 2, n, 2):
            if condition(nums[j], nums[key_index]):
                key_index = j
        nums[i], nums[key_index] = nums[key_index], nums[i]


nums = [1, 3, 5, 7]
sort_by_index(nums)
print(nums)