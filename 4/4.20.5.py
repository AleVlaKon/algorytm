def count_solutions(n):
    counter = 0
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if n - 3 * x - 2 * y > 0:
            # for z in range(1, n + 1):
            #     print(x, y, z)
            #     if 3*x + 2*y + z == n:
                    counter += 1
                    # print('-----')
    return counter


print(count_solutions(10))
print(count_solutions(5))    # 3x + 2y + z = 5
print(count_solutions(20))
print(count_solutions(1))