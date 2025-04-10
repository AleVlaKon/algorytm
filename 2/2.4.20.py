def equation_of_line(values: list[int]) -> str:
    coords = tuple(enumerate(values))
    x1, y1 = coords[0]
    x2, y2 = coords[1]
    k = int((y2 - y1) / (x2 - x1))
    b = int((y1 * x2 - x1 * y2) / (x2 - x1))

    first_part = ''
    second_part = ''
    if k == -1:
        first_part = '-x'
    elif k == 1:
        first_part = 'x'




print(equation_of_line([0, 1, 2, 3, 4]))
print(equation_of_line([0, -1, -2, -3, -4]))