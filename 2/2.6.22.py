from math import sqrt

def solve_quadritic(a: int, b: int, c: int) -> set:
    discriminant = b ** 2 - 4 * a * c

    if discriminant >= 0:
        x1 = (-b + sqrt(discriminant))/(2 * a)
        x2 = (-b - sqrt(discriminant))/(2 * a)
        if x1 == 0:
            x1 = abs(x1)
        if x2 == 0:
            x2 = abs(x2)
        result = {x1, x2}
    else:
        result = set()

    return result

def solve_linear(b: int, c: int) -> set:
    x = -c/b
    if x == 0:
        x = abs(x)    
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
    elif result_b:
        result_x = solve_linear(result_b, result_c)
    else:
        result_x = set()
        
    if len(result_x) == 2:
        x1, x2 = list(result_x)
        y1 = a1 * x1 ** 2 + b1 * x1 + c1
        y2 = a2 * x2 ** 2 + b2 * x2 + c2
        result = {(x1, y1), (x2, y2)}
    if len(result_x) == 1:
        x = list(result_x)[0]
        y = a1 * x ** 2 + b1 * x + c1
        result = {(x, y)}

    return result
    
    

