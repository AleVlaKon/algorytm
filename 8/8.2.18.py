def k_swaps_to_sort(n, k):

    nums = list(range(1, n + 1))

    for i in range(n - 1):
        for j in range(n - i - 1):
            if k == 0:
                break
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                k -= 1
    
    return nums


print(k_swaps_to_sort(10, 45))
print(k_swaps_to_sort(5, 10))
print(k_swaps_to_sort(5, 1))
print(k_swaps_to_sort(1, 0))
print(k_swaps_to_sort(5, 3))