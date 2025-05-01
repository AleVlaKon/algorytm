import math


def closest_exponent(n: int) -> int:
    log_2_n = math.log2(n)
    return math.ceil(log_2_n)


print(closest_exponent(8))     # 2^3 = 8 >= 8
print(closest_exponent(13))    #  2^4 = 16 >= 13
print(closest_exponent(28))    # 2^5 = 32 >= 28
print(closest_exponent(64))    # 2^6 = 64 >= 64
print(closest_exponent(1))     # 2^0 = 1 >= 1
print(closest_exponent(10))    # 2^4 = 16 >= 10