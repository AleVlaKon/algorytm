def count_solutions(n):
    counter = 0
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if n - 3 * x - 2 * y > 0:
                counter += 1
    return counter