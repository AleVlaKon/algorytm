def exponential_binary_search(data, target):     # data – набор чисел, target – искомое число
    right = 1

    while data[right] < target:
        right *= 2
        
    left = right // 2
    
    while left <= right:
        middle = (left + right) // 2
        elem = data[middle]
        if elem == target:
            return True
        if elem < target:
            left = middle + 1
        else:
            right = middle - 1

    return False

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 1
exponential_binary_search(data, target)