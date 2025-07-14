def drop_digit(digits: str) -> str:
    for i in range(len(digits) - 1):
        if digits[i] < digits[i+1]:
            return digits[:i] + digits[i+1:]
    return digits[:-1]

print(drop_digit('27'))
print(drop_digit('123'))
print(drop_digit('9614'))
print(drop_digit('10'))
print(drop_digit('11111'))