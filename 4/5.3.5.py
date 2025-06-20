from math import floor


def fizz_buzz(n: int) -> tuple:
    new_n = n - 1
    to_fifteen = floor(new_n / 15)
    to_three = floor(new_n / 3) - to_fifteen
    to_five = floor(new_n / 5) - to_fifteen
    return to_three, to_five, to_fifteen



print(fizz_buzz(20))

print(fizz_buzz(5))
print(fizz_buzz(31))