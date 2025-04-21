import itertools
from typing import Any, Tuple


def polynomial_sum(p1: Tuple[int], p2: Tuple[int]) -> Tuple[Any, ...]:
    zip_result = itertools.zip_longest(reversed(p1), reversed(p2), fillvalue=0)
    reversed_result_with_zeros = list(x + y for x, y in zip_result)[::-1]
    result_without_zeros = itertools.dropwhile(lambda x: x == 0, reversed_result_with_zeros)

    return tuple(result_without_zeros)



p1 = (2, -4, 5)                  # P1(x) = 2x^2 - 4x + 5
p2 = (3, 2)                      # P2(x) = 3x + 2

print(polynomial_sum(p1, p2))    # P1(x) + P2(x) = 2x^2 - x + 7


p1 = (1, 7, 0, -4)               # P1(x) = x^3 + 7x^2 - 4
p2 = (-1, 0, 0, 2)               # P2(x) = -x^3 + 2

print(polynomial_sum(p1, p2))    # P1(x) + P2(x) = 7x^2 - 2