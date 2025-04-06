def get_quadrant(p: tuple[int]) -> int:
    x, y = p
    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    if x > 0 and y < 0:
        return 4
    



if __name__ == "__main__":
    print(get_quadrant((0, 3)))
    print(get_quadrant((3, 0)))
    print(get_quadrant((3, 4)))
    print(get_quadrant((-1, 2)))
    print(get_quadrant((-3, -5)))
    print(get_quadrant((1, -1)))
