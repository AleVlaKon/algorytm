import itertools
from typing import Any, Tuple


def polynomial_sum(p1: Tuple[int], p2: Tuple[int]) -> Tuple[Any, ...]:
    zip_result = itertools.zip_longest(reversed(p1), reversed(p2), fillvalue=0)
    reversed_result_with_zeros = list(x + y for x, y in zip_result)[::-1]
    result_without_zeros = itertools.dropwhile(lambda x: x == 0, reversed_result_with_zeros)

    return tuple(result_without_zeros)
