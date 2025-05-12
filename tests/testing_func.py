import math


def rotate_number(number: int) -> int:
    new_digit = 0
    log_n = math.log10(number)
    len_number = math.floor(log_n) + 1
    for i in range(len_number - 1, -1, -1):
        last_digit = number % 10
        new_digit += last_digit * 10 ** i
        number //= 10
    return new_digit


def make_palindrome(n: int):
    if n == rotate_number(n):
        return n
    else:
        new_n = n
        for i in range(5):
            rotated_num = rotate_number(new_n)
            new_n += rotated_num
            if new_n == rotate_number(new_n):
                return new_n


    return -1