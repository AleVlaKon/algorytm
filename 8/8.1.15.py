def selection_sort(nums: list) -> None:
    len_nums = len(nums)

    for i in range(len_nums - 1):
        min_index = i

        for j in range(i + 1, len_nums):
            if nums[j] > nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]


nums = [3, 2, 2, 1, 3, 3]
selection_sort(nums)
print(nums)