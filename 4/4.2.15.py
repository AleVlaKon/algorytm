def rotate_number(number: int) -> int:
    new_digit = 0
    while number > 0:
        last_digit = number % 10
        new_digit = new_digit * 10 + last_digit
        number //= 10
    return new_digit


def make_palindrome(n: int):
    for i in range(6):
        new_n = rotate_number(n)
        if new_n == n:
            return new_n
        else:
            n += new_n


    return -1




print(make_palindrome(166))
