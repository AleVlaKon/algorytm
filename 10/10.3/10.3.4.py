def move_zeros(nums: list[int]):
   left = 0

   for right in range(len(nums)):
      if nums[right] != 0:
         nums[left], nums[right] = nums[right], nums[left]
         left += 1



nums = [0, 2, 0, 0, 1]
move_zeros(nums)
print(nums)

