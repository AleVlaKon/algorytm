def one_truth(flags: list):
    return sum(flags) == 1


print(one_truth([True, False, False]))
print(one_truth([True, False, True]))
print(one_truth([False, False, False, False, False]))