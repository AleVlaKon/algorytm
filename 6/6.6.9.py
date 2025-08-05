def binary_search(data, target):
    left, right = 0, len(data) - 1
    while left <= right:
        middle = (left + right) // 2
        elem = data[middle]
        if elem == target:
            return middle
        if elem < target:
            left = middle + 1
        if elem > target:
            right = middle - 1
    return -1

print(binary_search([10, 20, 30, 40, 50], 40))