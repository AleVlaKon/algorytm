def restore_by_prefix_sum(p: list) -> list[int]:
    result = [p[i] - p[i - 1] for i in range(1, len(p))]
    return result

print(restore_by_prefix_sum([0, 10, 14, 20, 21, 29]))
print(restore_by_prefix_sum([0, 1, 3, 6, 10, 15]))