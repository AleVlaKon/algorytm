def sort_numbers_from_one_to_three(nums: list[int]) -> None:
    left = 0
    current = 0
    right = len(nums) - 1

    while current <= right:
        if nums[current] == 1:
            nums[left], nums[current] = nums[current], nums[left]
            left += 1
            current += 1

        elif nums[current] == 2:
            current += 1

        elif nums[current] == 3:
            nums[right], nums[current] = nums[current], nums[right]
            right -= 1

nums = [2, 1, 3, 1, 3, 1, 3, 3]
sort_numbers_from_one_to_three(nums)
print(nums)
        