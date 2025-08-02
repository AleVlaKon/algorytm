from itertools import pairwise


def min_difference(num: int) -> int:
    deliteli = []
    i = 1
    while i <= num: 
        if num % i == 0:
            deliteli.append(i)
        i += 1
    min_del = num

    for i, j in pairwise(deliteli):
        if j - i < min_del:
            min_del = j - i

    return min_del

print(min_difference(2))
print(min_difference(143))


