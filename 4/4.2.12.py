def sum_digits(n: int):
    summ = 0
    while n > 0:
        summ += n % 10
        n //= 10
    return summ

def min_digit_sum(a, b):
    count = 0
    min_sum = 10 ** 6
    for i in range(a, b + 1):
        res = sum_digits(i)    
        if res < min_sum:
            min_sum = res
            count = 1
        elif res == min_sum:
            count += 1
    return count

print(min_digit_sum(1, 50))
print(min_digit_sum(1, 100))
print(min_digit_sum(50, 200))
print(min_digit_sum(1, 1000))