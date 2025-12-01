def cocktail_sort(nums):
    n = len(nums)
    left = 0
    right = n


    for i in range(n // 2):
        for j in range(left, right - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

        for j in range(right - 1, left, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
        left += 1
        right -= 1

data = [1, 1, 1, 1, 1]
cocktail_sort(data)
print(data)