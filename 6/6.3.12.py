def max_nearby_product(nums):
    max_composition = float('-inf')
    for i in range(1, len(nums)):
        if nums[i] * nums[i-1] > max_composition:
            max_composition = nums[i] * nums[i-1]

    return max_composition


print(max_nearby_product([3, 1, 6, 4, -2, -7]))            # 6 и 4
print(max_nearby_product([0, -1, 1, 24, 1, 8, 10, -4]))    # 8 и 10