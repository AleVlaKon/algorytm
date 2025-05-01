import math


def count_digits(n: int) -> int:
    log_n = math.log10(n)
    number_of_digits = math.floor(log_n) + 1
    return number_of_digits






print(count_digits(12345))

print(count_digits(2))
print(count_digits(10 ** 100))
print(count_digits(4 ** 55))

print(count_digits(9))
print(count_digits(2 ** 1000))