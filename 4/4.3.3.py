def parse_max(s: str):
    list_of_digits = []
    if s[0].isdigit():
        list_of_digits.append(s[0])
    for i in range(1, len(s)):
        if s[i-1].isdigit() and s[i].isdigit():
            list_of_digits[-1] += s[i]
        elif s[i].isdigit():
            list_of_digits.append(s[i])
    if not  list_of_digits:
        return -1

    return max(int(i) for i in list_of_digits)


print(parse_max('01ab2c3d04'))
