from itertools import accumulate
from operator import mul

def product_in_segments(nums, segments):
    total = list(accumulate(nums, mul, initial=1))

    result = [total[r + 1] // total[l] for l, r in segments]

    return result


print(product_in_segments([2, 6, 1, 4, 2], [(0, 2), (1, 4)]))           # 2*6*1 = 12; 6*1*4*2 = 48
print(product_in_segments([1], [(0, 0)]))
print(product_in_segments([1, 3, 2, 4], [(0, 1), (0, 3)]))              # 1*3 = 3; 1*3*2*4 = 24
print(product_in_segments([1, 1, 1, 1, 1], [(0, 1), (1, 2), (2, 3)]))   # 1*1 = 1; 1*1 = 1; 1*1 = 1