def wave(nums: list[int]) -> None:
    for i in range(1, len(nums)):
        if i % 2 == 0 and nums[i-1] > nums[i]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
        elif i % 2 == 1 and nums[i-1] < nums[i]:
            nums[i], nums[i-1] = nums[i-1], nums[i]


data = [1, 2, 3, 4, 5]
wave(data)
print(data)

data = [2, 4, 7, 8, 9, 10]
wave(data)
print(data)