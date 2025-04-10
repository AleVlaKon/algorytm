def on_one_line(p1: tuple[int], p2: tuple[int], p3: tuple[int]) -> bool:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    k = (y2 - y1) / (x2 - x1)
    b = (y1 * x2 - x1 * y2) / (x2 - x1)
    return  k * x3 + b == y3

print(on_one_line((1, 1), (2, 2), (3, 3)))
print(on_one_line((1, 1), (2, 2), (3, 4)))
print(on_one_line((1, 2), (2, 2), (3, 2)))
print(on_one_line((-1, -2), (-2, -2), (-3, -2)))
print(on_one_line((0, 0), (1, 1), (2, 2)))
print(on_one_line((1, 1), (0, 0), (-10, -10)))
