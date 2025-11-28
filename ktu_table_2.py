import numpy as np

import pandas as pd



def generate_constrained_matrix(rows=44, cols=33, min_nonzero=6, max_nonzero=8):
    """
    Генерирует матрицу где:
    - сумма каждой строки = 1
    - сумма каждого столбца = 1
    - в каждой строке от 6 до 8 ненулевых элементов
    """
    
    matrix = np.zeros((rows, cols))
    
    # Шаг 1: Определяем количество ненулевых элементов в каждой строке
    nonzero_per_row = np.random.randint(min_nonzero, max_nonzero + 1, rows)
    
    # Шаг 2: Инициализируем матрицу случайными значениями
    for i in range(rows):
        # Выбираем случайные позиции для ненулевых элементов
        nonzero_positions = np.random.choice(cols, nonzero_per_row[i], replace=False)
        
        # Генерирем случайные положительные числа для этих позиций
        random_values = np.random.dirichlet(np.ones(nonzero_per_row[i]))
        
        # Записываем значения в матрицу
        matrix[i, nonzero_positions] = random_values
    
    # Шаг 3: Нормализуем чтобы суммы строк и столбцов были равны 1
    # Используем итеративный метод Sinkhorn-Knopp
    max_iterations = 1000
    tolerance = 1e-6
    
    for iteration in range(max_iterations):
        # Нормализуем строки
        row_sums = matrix.sum(axis=1)
        matrix = matrix / row_sums[:, np.newaxis]
        
        # Нормализуем столбцы
        col_sums = matrix.sum(axis=0)
        matrix = matrix / col_sums[np.newaxis, :]
        
        # Проверяем сходимость
        row_error = np.max(np.abs(matrix.sum(axis=1) - 1))
        col_error = np.max(np.abs(matrix.sum(axis=0) - 1))
        
        if row_error < tolerance and col_error < tolerance:
            break
    
    return matrix

# Генерируем матрицу
result_matrix = generate_constrained_matrix()



df = pd.DataFrame(result_matrix)

# Сохраняем в Excel
df.to_excel('matrix_2.xlsx', index=False, header=False)

# Или с индексами и заголовками
df.to_excel('matrix_with_headers_2.xlsx', 
            index=True, 
            header=True,
            index_label='Строка',
            sheet_name='Матрица')