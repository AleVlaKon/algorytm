from math import log10, floor

def drop_one_and_five(n):
    new_n = 0
    if n:
        len_n = floor(log10(n)) + 1
        for power in range(len_n, 0, -1):
            ten_in_power = 10 ** (power - 1)
            left_digit = n // ten_in_power
            if left_digit not in (1, 5):
                new_n += left_digit * ten_in_power
            else:
                new_n //= 10
            n = n % ten_in_power
    return new_n


print(drop_one_and_five(10))

