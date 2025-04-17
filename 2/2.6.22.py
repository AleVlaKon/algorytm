def solve_quadritic(a: int, b: int, c: int) -> set:
    discriminant = b ** 2 - 4 * a * c

    result = set()
    
    if discriminant >= 0:
        for i in (1, -1):
            x = (-b + i * discriminant ** 0.5)/(2 * a)
            result.add(x)

    return result

def solve_linear(b: int, c: int) -> set:
    x = -c/b
    y = b * x + c
    result = set()
    
    return 


def quadratic_intersections(
        a1: int,
        b1: int,
        c1: int,
        a2: int,
        b2: int,
        c2: int,
):
    result_a = a1 - a2
    result_b = b1 - b2
    result_c = c1 - c2

    discriminant = result_b ** 2 - 4 * result_a * result_c
    result = set()
    if discriminant >= 0:
        x1 = (-result_b + discriminant ** 0.5)/(2 * result_a)
        y1 = a1 * x1 ** 2 + b1 * x1 + c1
        x2 = (-result_b - discriminant ** 0.5)/(2 * result_a)
        y2 = a1 * x2 ** 2 + b1 * x2 + c1

        result.add((x1, y1))
        result.add((x2, y2))
    
    return result
    
    


print(quadratic_intersections(1, -2, 1, -1, -1, 7))
print(quadratic_intersections(1, 0, 0, -1, 0, 0))
print(quadratic_intersections(1, 2, 3, 4, 5, 6))
print(quadratic_intersections(-1, 0, 0, 3, -2, -2))
print(quadratic_intersections(-1, 0, 2, 3, 0, 2))
print(quadratic_intersections(1, 2, 0, 1, 4, 0))