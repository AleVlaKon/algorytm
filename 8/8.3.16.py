def binary_search(nums, k):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle_idx = (left + right) // 2
        center_elem = nums[middle_idx]

        if k == center_elem:
            return middle_idx
        if k > center_elem:
            left = middle_idx + 1
        if k < center_elem:
            right = middle_idx - 1

    return left


# nums = [1, 2, 4, 5]
# print(binary_search(nums, 3))
# print(binary_search(nums, 4))
# print(binary_search(nums, 5))
# print(binary_search(nums, 6))
# print(binary_search(nums, 0))
        

def binary_insertion_sort(nums):
    n = len(nums)

    for i in range(n):
        element = nums[i]
        incert_position = binary_search(nums[:i], element)

        for j in range(i - 1, incert_position - 1, -1):
            nums[j + 1] = nums[j]


        nums[incert_position] = element
            
nums = [3, 2, 2, 1, 3, 3]
binary_insertion_sort(nums)
print(nums)

        
        