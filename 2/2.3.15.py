from typing import Callable

def draw_field():
    # draw field 34x12
    field = [[' ']* 34 for i in range(12)]
    n = 9
    for i in field[1:10]:
        i[2] = '|'
        i[0] = n
        n -= 1
    n = 1
    for i in range(5, 30, 3):
        field[11][i] = n
        n += 1
    for i in range(3, 30):
        field[10][i] = '-'

    field[10][31] = '>'
    field[10][33] = 'x'
    field[0][0] = 'y'
    field[0][2] = '^'
    field[10][2] = '+'

    return field




def draw_graph(f: Callable):
    field = draw_field()
    for i in range(1, 10):
        x_coord = 2 + i * 3
        y_coord = 10 - f(i)
        if y_coord >= 1:
            field[y_coord][x_coord] = '*'
    for i in field:
        print(*i, sep='')

def f(x):
    if x in (1, 2):
        return 1
    return f(x - 1) + f(x - 2)

draw_graph(f)