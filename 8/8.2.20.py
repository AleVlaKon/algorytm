
def sum_of_five_largest_and_smallest(nums):
    n = len(nums)
    left = 0
    right = n


    for i in range(5):
        for j in range(left, right - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

        for j in range(right - 1, left, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
        left += 1
        right -= 1

    return sum(nums[-5:]), sum(nums[:5])

print(sum_of_five_largest_and_smallest([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(sum_of_five_largest_and_smallest([7, -5, -7, -5, 5, -1, 6, -6, -10, 3, -1, 3]))
print(sum_of_five_largest_and_smallest([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(sum_of_five_largest_and_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))