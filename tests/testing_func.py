def is_perfect_possible(keys: list[str], answers: list[str]) -> bool:
    first_compare = keys[0] == answers[0]
    for key, answer in zip(keys[1:], answers[1:]):
        if key == '*':
            continue
        compare_result = key == answer
        if first_compare != compare_result:
            return False
    return True