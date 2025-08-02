def max_of_two(a, b):
    if a < b:
        return b
    return a


def max_of_four(a, b, c, d):
    return max_of_two(max_of_two(a, b), max_of_two(b, c))

print(max_of_four(1, 2, 3, 1))
print(max_of_four(1, 1, 1, 1))
print(max_of_four(4, 5, 1, 3))
