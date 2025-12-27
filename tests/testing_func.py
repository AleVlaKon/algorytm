from itertools import accumulate
from operator import mul

def product_in_segments(nums, segments):
    total = list(accumulate(nums, mul, initial=1))

    result = [total[r + 1] // total[l] for l, r in segments]

    return result