def binary_search(data, target):        # data – список чисел, target – искомое число
    left, right = 0, len(data) - 1
    while left <= right:
        middle = (left + right) // 2
        elem = data[middle]
        if elem == target:
            return middle
        if elem > target:
            left = middle + 1
        else:
            right = middle - 1
    return -1 
