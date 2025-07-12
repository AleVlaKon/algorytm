def add_one(digits: list[int]) -> list[int]:
    if digits[-1] != 9:
        digits[-1] += 1
        return digits
    else:
        digits[-1] += 1


    for i in range(len(digits) -1, 0, -1):
        if digits[i] == 10:
            digits[i] = 0
            digits[i - 1] += 1

    if digits[0] == 10:
        digits[:1] = [1, 0]

    return digits



print(add_one([9, 9, 9]))
print(add_one([1, 2, 3]))    # число 123