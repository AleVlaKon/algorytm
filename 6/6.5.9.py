def third_max_value(nums):
    first_max = float('-inf')
    second_max = float('-inf')
    third_max = float('-inf')
    for num in nums:
        if num > first_max:
            third_max = second_max
            second_max = first_max 
            first_max = num
        elif num > second_max:
            third_max = second_max 
            second_max = num
        elif num > third_max:
            third_max = num
    return third_max


print(third_max_value([4, 8, 6, 10]))