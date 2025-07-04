def algorytm(n):
    count = 0
    while n > 1:
        n /= 9
        count += 1
        print(count)
    return n == 1


algorytm(9 ** 15 + 8)