def insertion_sort(nums):
    n = len(nums)

    for i in range(n - 2, -1, -1):
        item = nums[i]
        j = i + 1

        while j < n and item < nums[j]:
            nums[j - 1] = nums[j]
            j += 1

        nums[j - 1] = item


nums = [3, 2, 2, 1, 3, 3]
insertion_sort(nums)
print(nums)

            
