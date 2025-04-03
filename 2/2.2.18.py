def calculate(vars: str, values: list[int], exp: str) -> int:
    combination_values = zip(vars, values)
    dict_of_values = {k: v for k, v in combination_values}
    result = eval(exp, dict_of_values)
    return result



if __name__ == "__main__":
    calculate('ab', [2, 2], 'a+b')