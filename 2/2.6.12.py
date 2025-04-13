def quadratic_values(a: int, b: int, c: int, start: int=0, step: int=1) -> list[tuple]:
    result = []
    for i in range(10):
        x_i = start + i * step
        y_i = a * x_i ** 2 + b * x_i + c
        result.append((x_i, y_i))
    return result

print(quadratic_values(-1, -1, -1))