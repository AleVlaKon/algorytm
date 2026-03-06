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
