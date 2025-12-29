from itertools import accumulate


def difference_list(nums):
    total = list(accumulate(nums, initial=0))
    result = []

    for i in range(1, len(total)):
        last = len(total) - 1
        sum_right = total[last] - total[i]
        sum_left = total[i - 1]
        result.append(abs(sum_left - sum_right))
        # print(f'|{sum_left} - {sum_right}|')

    return result


print(difference_list([2, 3, 6, 1, 4]))    # |0 - 14| = 14; |2 - 11| = 9; |5 - 5| = 0;
                                           # |11 - 4| = 7; |12 - 0| = 12

print(difference_list([1, 2, 3, 4, 5]))    # |0 - 14| = 14; |1 - 12| = 11; |3 - 9| = 6;
                                           # |6 - 5| = 1; |10 - 0| = 10

print(difference_list([1]))                # |0 - 0| = 0;