def max_of_two(a, b):
    if a < b:
        return b, a
    return a, b


def golden_pairs(pairs: tuple[int, int]):
    count =0
    for x, y in pairs:
        x_1, y_1 = max_of_two(x, y)

        if 1.6 <= x_1 / y_1 <= 1.7:
            count += 1
    return count


print(golden_pairs([(100, 165), (180, 100), (170, 100), (100, 160)]))