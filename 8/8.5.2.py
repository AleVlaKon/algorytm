def find_triple(nums: list[int]):
    nums.sort(reverse=True)

    return [nums[0] - nums[i] for i in range(1, 4)]

print(find_triple([8, 5, 7, 4]))




