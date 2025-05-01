from math import log10, floor

def count_powers(num: int) -> int:
    num2 = 0
    power = 0
    while num2 != num:
        power += 1
        num2 = next_power_of_two(power)
    return power


def next_power_of_two(power: int) -> int:
    result = 0
    for i in range(1, power + 1):
        len_i_to_the_power = floor(i * log10(2)) + 1
        result = result * 10 ** (len_i_to_the_power) + 2 ** i
    return result
        


# print(next_power_of_two(7))



print(count_powers(2))  #1
print(count_powers(24)) #2
print(count_powers(248))  #3
print(count_powers(24816))  #4
print(count_powers(2481632))  #5
print(count_powers(248163264))  #6
print(count_powers(248163264128))   #7
print(count_powers(248163264128256))   #8