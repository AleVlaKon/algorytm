def swap_digits(n: int) -> int:
    return (n % 10) * 100 + (n % 100) - (n % 10) + n // 100


    # result = [0, 0, 0]

    # result[0] = (n % 10) * 100
    # result[2] = n // 100
    # result [1] = (n % 100) - (n % 10)

    # return result


print(swap_digits(321))