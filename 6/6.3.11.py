def sum_digits(num: int):
    num = abs(num)
    count = 0
    while num > 0:
        last_digit = num % 10
        count += last_digit
        num //= 10

    return count

def max_digits_sum(nums):
    max_num = 0
    max_sum_digits = 0
    for num in nums:
        sum_num_digit = sum_digits(num)
        if (sum_num_digit, num) > (max_sum_digits, max_num):
            max_sum_digits, max_num = sum_num_digit, num

    return max_num


print(max_digits_sum([10, 15, 22, 27, 14, 25]))
print(max_digits_sum([10, 15, 1, 51, 6, 11]))
print(max_digits_sum([50, 0, 14, -2, 22, 41]))
print(max_digits_sum([-11]))
print(max_digits_sum([-10, 10]))
print(max_digits_sum([1, 1, 1]))
print(max_digits_sum([30, 300, -3000]))