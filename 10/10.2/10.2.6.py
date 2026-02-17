
from collections import defaultdict

def radix_sum(n):
    first_dict = defaultdict(int)

    for a in range(10 ** 6):
        sum_digit = 0
        while a > 0:
            last = a % 10
            sum_digit += last
            a //= 10
        first_dict[sum_digit] += 1
    

    print(first_dict[0], first_dict[1], first_dict[2])

    count = 0
    for k in first_dict:
        k2 = n - k

        if k2 in first_dict:
            count += first_dict[k] * first_dict[k2]

    return count

print(radix_sum(1))         
print(radix_sum(2))