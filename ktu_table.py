import numpy as np
import pandas as pd


def generate_matrix_alternative(rows=44, cols=33, min_nonzero=6, max_nonzero=8):
    """
    Альтернативный подход с пошаговым заполнением
    """
    matrix = np.zeros((rows, cols))
    
    # Сначала распределяем "бюджет" по строкам
    for i in range(rows):
        nonzero_count = np.random.randint(min_nonzero, max_nonzero + 1)
        positions = np.random.choice(cols, nonzero_count, replace=False)
        
        # Начальные случайные значения
        values = np.random.dirichlet(np.ones(nonzero_count))
        matrix[i, positions] = values
    
    # Балансировка методом Sinkhorn
    return sinkhorn_balance(matrix)

def sinkhorn_balance(matrix, max_iter=1000, tol=1e-6):
    """Балансировка матрицы методом Sinkhorn"""
    mat = matrix.copy()
    
    for _ in range(max_iter):
        # Нормализация строк
        row_sums = mat.sum(axis=1)
        mat = mat / row_sums[:, np.newaxis]
        
        # Нормализация столбцов  
        col_sums = mat.sum(axis=0)
        mat = mat / col_sums[np.newaxis, :]
        
        # Проверка сходимости
        if (np.max(np.abs(mat.sum(axis=1) - 1)) < tol and 
            np.max(np.abs(mat.sum(axis=0) - 1)) < tol):
            break
    
    return mat

# Генерация и проверка
matrix = generate_matrix_alternative()

print("Проверка условий:")
print(f"Суммы строк: min={matrix.sum(axis=1).min():.6f}, max={matrix.sum(axis=1).max():.6f}")
print(f"Суммы столбцов: min={matrix.sum(axis=0).min():.6f}, max={matrix.sum(axis=0).max():.6f}")

nonzero_counts = (matrix > 0).sum(axis=1)
print(f"Ненулевые элементы в строках: min={nonzero_counts.min()}, max={nonzero_counts.max()}")



df = pd.DataFrame(matrix)

# Сохраняем в Excel
df.to_excel('matrix.xlsx', index=False, header=False)

# Или с индексами и заголовками
df.to_excel('matrix_with_headers.xlsx', 
            index=True, 
            header=True,
            index_label='Строка',
            sheet_name='Матрица')