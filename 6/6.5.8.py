def min_product_of_two(nums):
    first_min = float('inf')
    second_min = float('inf')
    for num in nums:
        if num < first_min:
            second_min = first_min
            first_min = num
        elif num < second_min:
            second_min = num
    return first_min * second_min


print(min_product_of_two([5, 2, 6, 1, 7]))
print(min_product_of_two([1, 1, 1, 1, 1]))
print(min_product_of_two([5, 4, 3, 2, 1]))
print(min_product_of_two([1, 5, 4, 3, 2]))
print(min_product_of_two([3, 4, 5, 2, 2]))
