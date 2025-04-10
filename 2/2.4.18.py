def linear_coefficients(p1: tuple[int], p2: tuple[int]) -> tuple[int]:
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    k = (y2 - y1) / (x2 - x1)
    b = (y1 * x2 - x1 * y2) / (x2 - x1)
    return k, b

print(linear_coefficients((1, 2), (2, 3)))
print(linear_coefficients((0, 0), (1, 5)))
print(linear_coefficients((0, 2), (2, 2)))
print(linear_coefficients((-2, -2), (-1, -2)))