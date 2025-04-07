

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


for i in draw_field():
    print(*i, sep='')

