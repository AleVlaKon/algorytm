def add_one(digits: list[int]):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits

    return [1] + digits


print(add_one([9, 9, 9]))
print(add_one([1, 2, 3]))    # число 123