def count_rescue_attempts(weights: list[int], limit: int):
    weights.sort()
    left = 0
    right = len(weights) - 1
    count = 0

    while left <= right:
        if weights[left] + weights[right] <= limit:
            left += 1
        right -= 1
        count += 1

    return count


print(count_rescue_attempts([1, 2], 3))
print(count_rescue_attempts([2, 3, 2, 1], 4))    # заходы: (2, 2), (1, 3)
print(count_rescue_attempts([3, 1, 2, 3], 4))    # заходы: (1, 3), (2), (3)
print(count_rescue_attempts([3, 2, 2, 3], 3))    # заходы: (3), (2), (2), (3)
print(count_rescue_attempts([50], 50))           # заходы: (50)
print(count_rescue_attempts([5, 5, 5, 5], 15))   # заход: (5, 5), (5, 5)