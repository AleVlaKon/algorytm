def binary_search(data, target):        # data – список чисел, target – искомое число
    left, right = 0, len(data) - 1
    while left <= right:
        middle = (left + right) // 2
        elem = data[middle]
        if elem == target:
            return left, right
        if elem < target:
            left = middle + 1
        else:
            right = middle - 1
    return left, right

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
