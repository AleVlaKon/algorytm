def format_coefficient(index: int, coefficient: int) -> str:
    sign = '+' if coefficient >= 0 else '-'
    if coefficient == 0:
        result = ''
    elif coefficient in (1, -1):
        result = f'{sign}x^{index}'
    else:
        result = f'{sign}{abs(coefficient)}x^{index}'
    if index == 0:
        result = result.replace('x^0', '')
    if index == 1:
        result = result.replace('x^1', 'x')
    return result


def polynomial(p) -> str:
    list_index_and_koefficients = enumerate(p[::-1], 0)
    list_of_elements = [format_coefficient(index, coefficient) for index, coefficient in list_index_and_koefficients]

    print(list_of_elements)
    result_str = ''.join(reversed(list_of_elements))
    if result_str.startswith('+'):
        result_str = result_str[1:]
    if result_str[-1] in ('+', '-'):
        result_str = result_str + '1'
    return result_str


print(polynomial((1, 3, -1, 1, -2)))
# print(polynomial((-2, 0, 1, -5)))
# print(polynomial((1, 0, 0, 0)))
# print(polynomial((1, 1, 1)))
# print(polynomial((-1, -1)))
# print(polynomial((-1,)))
# print(format_coefficient(5, 0))
# print(format_coefficient(5, 1))
# print(format_coefficient(5, 2))
# print(format_coefficient(5, -0))
# print(format_coefficient(5, -1))
# print(format_coefficient(5, -2))
