def cube_root(num: int):
    epsilon = 1 / 10 ** 6
    left, right = 0, num

    while right - left > epsilon:
        middle = (right + left) / 2

        if middle ** 3 < num:
            left = middle

        else:
            right = middle

    return ((left + right) / 2)


print(cube_root(8))