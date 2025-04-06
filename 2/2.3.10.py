def is_point_in_rectangle(p:tuple[int], rect: list[tuple]) -> bool:
    x, y = p
    x1, y1 = rect[0] 
    x2, y2 = rect[1]
    return x1 < x < x2 and y1 < y < y2







if __name__ == "__main__":
    print(is_point_in_rectangle((2, 2), [(1, 1), (3, 4)]))
    print(is_point_in_rectangle((1, 0), [(1, 1), (3, 4)]))
    print(is_point_in_rectangle((2, 1), [(1, 1), (3, 4)]))
    print(is_point_in_rectangle((0, 0), [(-1, -1), (3, 3)]))
    print(is_point_in_rectangle((3, 0), [(0, 0), (10, 1)]))
    print(is_point_in_rectangle((0, 0), [(0, 0), (0, 0)]))


