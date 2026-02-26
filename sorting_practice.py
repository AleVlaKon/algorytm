def incertion_sort(nums):
    n = len(nums)

    for i in range(n):
        element = nums[i]
        j = i - 1  # граница отсортированной части массива nums[:i]
        print(f'Элемент = {element}')
        print(f'Граница отсортированного массива от 0 до {j} (срез [:{j + 1}]')
        while j >= 0 and element < nums[j]:
            nums[j + 1] = nums[j]  # смещаем элемент "вперед"
            print(f'{element} < {nums[j]}')
            print(f'Элемент nums[{j}] смещается на {j + 1}')
            print(f'j уменьшается с {j}] до {j - 1}')
            j -= 1

        print(f'Вставляем элемент на позицию {j + 1}')
        nums[j + 1] = element  # как будто он упирается в меньший элемент и отпрыгивает обратно вправо
        print(f'------------------')

incertion_sort([9, 5, 7, 2, 7, 3])