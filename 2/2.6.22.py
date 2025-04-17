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
    return {x}


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

    result = set()
    
    if result_a:
        result_x = solve_quadritic(result_a, result_b, result_c)
    else:
        result_x = solve_linear(result_b, result_c)
    

    return result_x
    



print(quadratic_intersections(1, -2, 1, -1, -1, 7))
print(quadratic_intersections(1, 0, 0, -1, 0, 0))
print(quadratic_intersections(1, 2, 3, 4, 5, 6))
print(quadratic_intersections(-1, 0, 0, 3, -2, -2))
print(quadratic_intersections(-1, 0, 2, 3, 0, 2))
print(quadratic_intersections(1, 2, 0, 1, 4, 0))