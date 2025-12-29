def insertion_sort(data):                   # data – список чисел
    n = len(data)
    index = 0
    for i in range(1, n):
        item = data[i]
        j = i - 1

        while j >= 0 and item < data[j]:
            data[j + 1] = data[j]
            j -= 1
            index += 1

        data[j + 1] = item
    print(index)



insertion_sort([1, 3, 2, 5, 4, 7, 6, 8])