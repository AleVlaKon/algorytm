def calculate_sum(n):
    if n % 2 == 0:
        result = -(1 + n) / 2 * n
    else:
        result = -(1 + n - 1) / 2 * (n - 1) + n ** 2
    return int(result)
    

print(calculate_sum(4))
print(calculate_sum(9))