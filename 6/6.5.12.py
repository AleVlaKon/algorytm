def max_product_of_three(nums):
    first_max = float('-inf')
    second_max = float('-inf')
    third_max =  float('-inf')
    first_min = float('inf')
    second_min = float('inf')
    third_min = float('inf')
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
        if num < first_min:
            second_min = first_min 
            first_min = num
        elif num < second_min:
            second_min = num
    return max(first_max * second_max * third_max, first_min * second_min * first_max)

print(max_product_of_three([-5, -2, 4, 2, 4]))
print(max_product_of_three([-1, -2, -3]))