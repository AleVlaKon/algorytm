def max_sum(nums):
    max_num  = float('-inf')
    max_sum = 0
    for i in nums:
        if i > 0:
            max_sum += i
        if i > max_num:
            max_num = i
        
    return max_sum if max_sum > 0 else max_num

print(max_sum([-1, 10, 5]))         # 10 + 5