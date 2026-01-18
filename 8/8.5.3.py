def max_sum_of_k_elements(nums, k):
    sorted_nums = sorted(nums, reverse=True)
    return sum(sorted_nums[:k])


print(max_sum_of_k_elements([4, 2, 3, 1], 2))
print(max_sum_of_k_elements([-2, 4, 0, -3], 2))
