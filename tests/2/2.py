def is_point_in_rectangle(p:tuple[int], rect: list[tuple]) -> bool:
    x, y = p
    x1, y1 = rect[0] 
    x2, y2 = rect[1]
    return x1 < x < x2 and y1 < y < y2


def test_2_3_10():
    assert is_point_in_rectangle((2, 2), [(1, 1), (3, 4)]) == True
    assert is_point_in_rectangle((2, 2), [(1, 1), (3, 4)]) == True 
    assert is_point_in_rectangle((2, 1), [(1, 1), (3, 4)]) == False
    assert is_point_in_rectangle((0, 0), [(-1, -1), (3, 3)]) == True