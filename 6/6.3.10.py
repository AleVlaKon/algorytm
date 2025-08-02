def min_even_digit(num):
    min_digit = 10

    while num > 0:
        last_digit = num % 10
        if last_digit % 2 == 0 and last_digit < min_digit:
            min_digit = last_digit
        num //= 10

    if min_digit == 10:
        return -1
    else:
        return min_digit

print(min_even_digit(612))