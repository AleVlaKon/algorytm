def calculate_sum(n):
    last_digit = (n ** 2)
    result = last_digit / 2 * (n ** 2 + 1)
    return int(result)


print(calculate_sum(3))
print(calculate_sum(5))