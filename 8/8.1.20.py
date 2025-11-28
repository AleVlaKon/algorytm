
def sort_except_one(nums, a):
    n = len(nums)
    for i in range(n - 1):
        key_index = i

        for j in range(i + 1, n):
            if j == a or i == a:
                continue
            else:
                if nums[j] < nums[key_index]:
                    key_index = j
        nums[i], nums[key_index] = nums[key_index], nums[i]

nums = [5, 1, 3, 2, 4]
sort_except_one(nums, 4)
print(nums)