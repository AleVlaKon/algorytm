from math import log10, floor

def key_sort(num: int):
    if num != 0:
        count_digit = floor(log10(abs(num))) + 1
    else:
        count_digit = 1
    abs_num = num

    return count_digit, -abs_num


nums = [8, 13, 183, 9, 26, 229]
sort_by_length_and_value(nums)
print(nums)