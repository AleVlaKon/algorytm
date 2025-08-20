def triangle_of_coins(n: int) -> int:
    left, right = 1, n
    while left <= right:
        middle = (right + left) // 2
        num = (middle / 2) * (middle + 1)
        if num <= n:
            left = middle + 1
        else:
            right = middle - 1
    return right
    