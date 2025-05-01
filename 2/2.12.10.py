import math


def is_power_of_two(n: int) -> bool:
    return math.log2(n).is_integer()



print(is_power_of_two(16))
print(is_power_of_two(15))

print(is_power_of_two(1))
print(is_power_of_two(2))
print(is_power_of_two(100))
