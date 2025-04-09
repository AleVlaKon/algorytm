from typing import Callable


def draw_graph(f: Callable):
    print('y ^')
    for i in range(9, 0, -1):
        print(f'{i} |', end='')
        for x in range(1, 10):
            if f(x) == i:
                print('  *', end='')
            else:
                print('   ', end='')
        print()
    print('  +--------------------------- > x')
    print('     1  2  3  4  5  6  7  8  9')



def f(x):
    if x in (1, 2):
        return 1
    return f(x - 1) + f(x - 2)

draw_graph(f)