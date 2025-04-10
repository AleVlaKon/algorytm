def equation_of_line(values: list[int]) -> str:
    coords = tuple(enumerate(values))
    x1, y1 = coords[0]
    x2, y2 = coords[1]
    k = int((y2 - y1) / (x2 - x1))
    b = int((y1 * x2 - x1 * y2) / (x2 - x1))

    if not all(map((lambda x: k * x[0] + b == x[1]), coords)):
        return None

    if len(set(values)) == 1:
        return f'y = {values[0]}'

    if k == -1:
        first_part = '-x'
    elif k == 1:
        first_part = 'x'
    else:
        first_part = f'{k}x'

    if k == 0:
        second_part = f'b'
    elif b > 0:
        second_part = f'+ {b}'
    elif b < 0:
        second_part = f'- {abs(b)}'
    else:
        second_part = ''

    return f'y = {first_part} {second_part}'


print(equation_of_line([0, 1, 2, 3, 4]))
print(equation_of_line([0, -1, -2, -3, -4]))
print(equation_of_line([0, -2, -4, -6, -8]))
print(equation_of_line([1, 3, 5, 7, 9]))
print(equation_of_line([6, 6, 6, 6, 6]))
print(equation_of_line([1, 1, 2, 2, 2]))