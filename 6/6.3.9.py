def find_max_value(value: str):
    if value.isdigit():
        return int(value)
    else:
        return len(value)

def max_value(strings: list[str]) -> int:
    max_string_value = 0
    for string in strings:
        value = find_max_value(string)
        if value > max_string_value:
            max_string_value = value
    
    return max_string_value


print(max_value(['3', 'bee']))