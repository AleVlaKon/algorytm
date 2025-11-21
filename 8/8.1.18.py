def key_function(x):
    if isinstance(x, list):
        return x[0], True
    else:
        return x, False


def sort_like_nums(nums):
    n = len(nums)
    for i in range(n - 1):
        key_index = i
        for j in range(i + 1, n):
            if key_function(nums[j]) < key_function(nums[key_index]):
                key_index = j
        nums[i], nums[key_index] = nums[key_index], nums[i]


nums = [2, 1, [2], 3, [3]]
sort_like_nums(nums)
print(nums)