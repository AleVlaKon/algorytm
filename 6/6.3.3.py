def max_of_four(a, b, c, d):
    result = float('-inf')
    if a > result:
        result = a
    if b > result:
        result = b
    if c > result:
        result = c
    if d > result:
        result = d
    return result

print(max_of_four(1, 2, 3, 1))
print(max_of_four(1, 1, 1, 1))
print(max_of_four(4, 5, 1, 3))
