from itertools import accumulate


def difference_list(nums):
    total = list(accumulate(nums, initial=0))
    result = []

    for i in range(1, len(total)):
        last = len(total) - 1
        sum_right = total[last] - total[i]
        sum_left = total[i - 1]
        result.append(abs(sum_left - sum_right))


    return result


