def max_digit(num):
    result = 0
    while num > 0:
        digit = num % 10
        if digit > result:
            result = digit
        num //= 10
    return result



print(max_digit(1231))
print(max_digit(111))
print(max_digit(451))
