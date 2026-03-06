def count_rescue_attempts(weights: list[int], limit: int):
    sorted_weights = sorted(weights)
    left = 0
    right = len(weights) - 1
    count = 0

    while left <= right:
        if sorted_weights[left] + sorted_weights[right] <= limit:
            right -= 1
        else:
            left += 1
        right -= 1
        count += 1

    return count
