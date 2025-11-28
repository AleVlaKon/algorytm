def sort_by_parity(nums):
    n = len(nums)
    for i in range(n - 1):
        key_index = i
        if nums[i] % 2:
            for j in range(i + 1, n):
                if nums[j] % 2 and nums[j] < nums[key_index]:
                    key_index = j
        else:
            for j in range(i + 1, n):
                if nums[j] > nums[key_index] and not nums[j] % 2:
                    key_index = j

        nums[i], nums[key_index] = nums[key_index], nums[i]