def get_exam_position(n: int, k: int) -> int:
    if k % 2 != 0:
        return k // 2 + 1
    else:
        if n % 2 == 0:
            return n // 2 + k // 2
        else:
            return n // 2 + k // 2 + 1