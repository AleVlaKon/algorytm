def count_numbers(n: int, k: int):
    count = 0
    for i in range(1, n + 1):
        if i - sum_digit(i) >= k:
            count += 1
    return count


def sum_digit(n):
    sum_digit = 0
    while n > 0:
        sum_digit += n % 10
        n //= 10
    return sum_digit

print(count_numbers(13, 2))    # 10, 11, 12, 13
print(count_numbers(10, 5))    # 10
print(count_numbers(1, 0))     # 1
print(count_numbers(10, 0))     # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

