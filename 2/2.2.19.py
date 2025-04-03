def is_function(pairs:list[tuple]) -> bool:
    first_elements = [i[0] for i in pairs]
    return len(first_elements) == len(set(first_elements))


if __name__ == "__main__":
    print(is_function([(1, 3), (2, 5), (3, 7)]))
    print(is_function([(1, 3), (2, 5), (1, 7)]))
    print(is_function([(1, 3)]))
    print(is_function([(5, 5)]))
    print(is_function([(1, 1), (2, 2)]))
    print(is_function([(1, 1), (1, 2)]))