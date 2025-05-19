def is_perfect_possible(keys: list[str], answers: list[str]) -> bool:
    first_compare = keys[0] == answers[0]
    for key, answer in zip(keys[1:], answers[1:]):
        if key == '*':
            continue
        compare_result = key == answer
        if first_compare != compare_result:
            return False
    return True




print(is_perfect_possible(['A', 'B', 'C', '*', '*'], ['A', 'B', 'C', 'D', 'E']))    # True
print(is_perfect_possible(['A', 'B', 'C', '*', '*'], ['D', 'E', 'F', 'A', 'B']))    # True
print(is_perfect_possible(['A', 'B', 'B', '*', '*'], ['A', 'B', 'C', 'A', 'B']))    # False
print(is_perfect_possible(['A'], ['B']))    # True
print(is_perfect_possible(['*'], ['B']))    # True
print(is_perfect_possible(['*', 'A'], ['B', 'B']))    # True

