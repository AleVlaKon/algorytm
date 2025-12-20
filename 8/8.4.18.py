from collections import Counter


def sort_limited_numbers(data):
    min_value, max_value = min(data), max(data)
    counts = Counter(data)  # быстрое создание и заполнение вспомогательного словаря

    index = 0

    for num in range(max_value, min_value - 1, -1):
        for _ in range(counts.get(num, 0)):
            data[index] = num
            index += 1
