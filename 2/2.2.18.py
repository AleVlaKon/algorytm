def calculate(vars: str, values: list[int], exp: str) -> int:
    dict_of_values = dict(zip(vars, values))
    result = 0
    coef = 1
    for char in exp:
        if char == '-':
            coef = -1
        elif char == '+':
            coef = 1
        elif char in dict_of_values:
            result += dict_of_values[char]*coef
    return result



if __name__ == "__main__":
    print(calculate('ab', [2, 2], 'a+b'))