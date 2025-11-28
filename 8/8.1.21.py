
def sort_only_odds(nums):
    n = len(nums)
    for i in range(n - 1):
        key_index = i

        for j in range(i + 1, n):
            if nums[j] % 2 == 0 or nums[i] % 2 == 0:
                continue
            else:
                if nums[j] < nums[key_index]:
                    key_index = j
        nums[i], nums[key_index] = nums[key_index], nums[i]


nums = [3, 7, 5, 1, 9]
sort_only_odds(nums)
print(nums)

nums = [2, 8, 4, 0, 6]
sort_only_odds(nums)
print(nums)

nums = [-3, -8, -6, -5, -4, -1]
sort_only_odds(nums)
print(nums)