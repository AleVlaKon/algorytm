from math import log

def is_power_of_four(n: int) -> bool:
    return log(n, 4).is_integer()


print(is_power_of_four(65))