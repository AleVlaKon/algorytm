def max_divider(nums):
    min_num = min(nums) 
    for num in nums:
      if num % min_num != 0:
         return -1
    return min_num


print(max_divider([8, 16, 20, 4, 12]))
print(max_divider([3, 5, 7, 9, 11]))
print(max_divider([1, 2, 3, 4, 5]))