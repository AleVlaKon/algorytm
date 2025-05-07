def mystery(n):
    result = 0
    if n == 0:
        result = 1
    while n > 0:
        last_digit = n % 10
        if last_digit in (6, 9, 0):
            result += 1
        if last_digit == 8:
            result += 2
        n //= 10
    return result