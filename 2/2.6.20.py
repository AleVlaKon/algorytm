def solve(a: int, b: int, c: int) -> set:
    discriminant = b ** 2 - 4 * a * c

    result = set()
    
    if discriminant >= 0:
        for i in (1, -1):
            x = (-b + i * discriminant ** 0.5)/(2 * a)
            result.add(x)

    return result


print(solve(1, -5, 6))
print(solve(1, -2, 1))
print(solve(5, -2, 1))