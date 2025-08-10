def max_product_of_two(nums):
    first_max = float('-inf')
    second_max = float('-inf')
    first_min = float('inf')
    second_min = float('inf')
    for num in nums:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max:
            second_max = num

        if num < first_min:
            second_min = first_min
            first_min = num
        elif num < second_min:
            second_min = num
    return max(first_min * second_min, first_max * second_max)