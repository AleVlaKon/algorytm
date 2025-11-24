def alter_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        key_index = i
        if key_index % 2:
            for j in range(i + 1, n):
                if nums[j] < nums[key_index]:
                    key_index = j
            nums[i], nums[key_index] = nums[key_index], nums[i]
        else:
            for j in range(i + 1, n):
                if nums[j] > nums[key_index]:
                    key_index = j
            nums[i], nums[key_index] = nums[key_index], nums[i]



nums = [1, 2, 3, 4, 5]
alter_sort(nums)
print(nums)