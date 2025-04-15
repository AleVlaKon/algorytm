def quadratic(x1: int, x2: int):
    b = int(-x1 - x2)
    c = int(x1 * x2)
    operator_b = '-' if b < 0 else '+'
    operator_c = '-' if c < 0 else '+'
    if b == 0:
        second_part = ''
    elif abs(b) == 1:
        second_part = f' {operator_b} x'
    else:
        second_part = f' {operator_b} {abs(b)}x'
    third_part = f' {operator_c} {abs(c)}' if c else ''
    return f'x^2{second_part}{third_part} = 0'



print(quadratic(1, 2))
print(quadratic(0, 1))
print(quadratic(-3, 4))
print(quadratic(2, 0))
print(quadratic(0, 0))