def return_digits_of_n(n):
    digits = []
    while n > 0:
        last_digit = n % 10
        if last_digit != 0:
            digits.append(last_digit)
        n //= 10
    return digits



def divisible(n):
    count = 0
    for i in return_digits_of_n(n):
        if n != 0 and n % i == 0:
            count += 1
    return count


print(divisible(11))