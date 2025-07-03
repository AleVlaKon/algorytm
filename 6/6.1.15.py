def nine_divisors(n: int) -> int:
    final_count = 0
    for i in range(1, n+1):
        j_count = 0
        for j in range(1, i+1):
            if i % j == 0:
                j_count += 1
        if j_count == 9:
            final_count += 1
    return final_count

print(nine_divisors(100))     # 36, 100
print(nine_divisors(10))
print(nine_divisors(50))     # 36
print(nine_divisors(300))    # 36, 100, 196, 225, 256