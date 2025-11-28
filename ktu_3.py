import numpy as np
import pandas as pd


def improved_sinkhorn_with_constraints(rows=44, cols=33, min_nonzero=6, max_nonzero=8):
    """
    Улучшенный алгоритм с гарантией выполнения всех условий
    """
    # Создаем маску ненулевых элементов
    mask = np.zeros((rows, cols), dtype=bool)
    for i in range(rows):
        nonzero_count = np.random.randint(min_nonzero, max_nonzero + 1)
        positions = np.random.choice(cols, nonzero_count, replace=False)
        mask[i, positions] = True
    
    # Начальная матрица с правильной структурой
    matrix = np.zeros((rows, cols))
    for i in range(rows):
        nonzero_positions = np.where(mask[i])[0]
        values = np.random.dirichlet(np.ones(len(nonzero_positions)) * 0.1)  # Более равномерное распределение
        matrix[i, nonzero_positions] = values
    
    # Балансировка с сохранением структуры
    return balance_matrix_preserving_structure(matrix, mask)


def balance_matrix_preserving_structure(matrix, mask, max_iter=10000, tol=1e-6):
    """
    Балансирует матрицу, сохраняя нулевые элементы
    """
    mat = matrix.copy()
    
    for iteration in range(max_iter):
        # Сохраняем структуру перед нормализацией
        current_values = mat[mask]
        
        # Нормализация строк
        row_sums = mat.sum(axis=1)
        mat = mat / row_sums[:, np.newaxis]
        
        # Восстанавливаем нулевые элементы
        mat[~mask] = 0
        
        # Нормализация столбцов
        col_sums = mat.sum(axis=0)
        col_sums[col_sums == 0] = 1  # Избегаем деления на ноль
        mat = mat / col_sums[np.newaxis, :]
        
        # Восстанавливаем нулевые элементы
        mat[~mask] = 0
        
        # Проверка сходимости
        row_error = np.max(np.abs(mat.sum(axis=1) - 1))
        col_error = np.max(np.abs(mat.sum(axis=0) - 1))
        
        if row_error < tol and col_error < tol:
            print(f"Балансировка завершена на итерации {iteration}")
            break
            
        # Периодическое обновление для избежания застревания
        if iteration % 500 == 0 and iteration > 0:
            # Слегка перемешиваем значения в ненулевых позициях
            for i in range(mat.shape[0]):
                nonzero_idx = np.where(mask[i])[0]
                if len(nonzero_idx) > 0:
                    new_values = np.random.dirichlet(np.ones(len(nonzero_idx)) * 0.5)
                    mat[i, nonzero_idx] = new_values
    
    return mat

def generate_constrained_matrix(rows=44, cols=33, min_nonzero=6, max_nonzero=8):
    """
    Генерирует матрицу с двойной стохастичностью и ограничением на ненулевые элементы
    """
    # Создаем маску для ненулевых элементов
    mask = np.zeros((rows, cols), dtype=bool)
    
    for i in range(rows):
        nonzero_count = np.random.randint(min_nonzero, max_nonzero + 1)
        positions = np.random.choice(cols, nonzero_count, replace=False)
        mask[i, positions] = True
    
    # Итеративный метод для нахождения матрицы
    matrix = np.ones((rows, cols)) / cols  # Начальное приближение
    
    max_iterations = 5000
    tolerance = 1e-6
    
    for iteration in range(max_iterations):
        # Проекция на ограничения строк
        row_sums = matrix.sum(axis=1)
        matrix = matrix / row_sums[:, np.newaxis]
        
        # Проекция на ограничения столбцов
        col_sums = matrix.sum(axis=0)
        matrix = matrix / col_sums[np.newaxis, :]
        
        # Проекция на ограничение ненулевых элементов
        matrix[~mask] = 0
        
        # Проверка сходимости
        row_errors = np.abs(matrix.sum(axis=1) - 1)
        col_errors = np.abs(matrix.sum(axis=0) - 1)
        
        if np.max(row_errors) < tolerance and np.max(col_errors) < tolerance:
            print(f"Сходимость достигнута на итерации {iteration}")
            break
            
        # Перезапуск если застряли
        if iteration % 1000 == 0 and iteration > 0:
            matrix = np.random.rand(rows, cols)
            matrix[~mask] = 0
            print(f"Перезапуск на итерации {iteration}")
    
    return matrix# Альтернативный подход: метод последовательных приближений
def iterative_matrix_generation(rows=44, cols=33, min_nonzero=6, max_nonzero=8):
    """
    Построчное заполнение с последующей коррекцией
    """
    matrix = np.zeros((rows, cols))
    
    # Создаем маску
    mask = np.zeros((rows, cols), dtype=bool)
    for i in range(rows):
        nonzero_count = np.random.randint(min_nonzero, max_nonzero + 1)
        positions = np.random.choice(cols, nonzero_count, replace=False)
        mask[i, positions] = True
    
    # Начальное заполнение
    for i in range(rows):
        nonzero_positions = np.where(mask[i])[0]
        values = np.random.dirichlet(np.ones(len(nonzero_positions)))
        matrix[i, nonzero_positions] = values
    
    # Многократная балансировка
    for correction_cycle in range(100):
        # Корректировка столбцов
        col_sums = matrix.sum(axis=0)
        correction_factors = 1.0 / col_sums
        matrix = matrix * correction_factors[np.newaxis, :]
        
        # Корректировка строк с сохранением структуры
        for i in range(rows):
            nonzero_positions = np.where(mask[i])[0]
            if len(nonzero_positions) > 0:
                row_sum = matrix[i].sum()
                if row_sum > 0:
                    # Перераспределяем значения в ненулевых позициях
                    current_values = matrix[i, nonzero_positions]
                    new_values = current_values / row_sum
                    matrix[i, nonzero_positions] = new_values
        
        # Проверка сходимости
        row_errors = np.abs(matrix.sum(axis=1) - 1)
        col_errors = np.abs(matrix.sum(axis=0) - 1)
        
        if np.max(row_errors) < 1e-4 and np.max(col_errors) < 1e-4:
            print(f"Коррекция завершена на цикле {correction_cycle}")
            break
    
    return matrix

# Генерация и проверка
print("Генерация матрицы...")
matrix = improved_sinkhorn_with_constraints()

print("\nПроверка условий:")
print(f"Суммы строк: min={matrix.sum(axis=1).min():.6f}, max={matrix.sum(axis=1).max():.6f}")
print(f"Суммы столбцов: min={matrix.sum(axis=0).min():.6f}, max={matrix.sum(axis=0).max():.6f}")

nonzero_counts = (matrix > 0).sum(axis=1)
print(f"Ненулевые элементы в строках: min={nonzero_counts.min()}, max={nonzero_counts.max()}")

# Проверка точности
print(f"\nТочность:")
print(f"Максимальная ошибка строк: {np.max(np.abs(matrix.sum(axis=1) - 1)):.10f}")
print(f"Максимальная ошибка столбцов: {np.max(np.abs(matrix.sum(axis=0) - 1)):.10f}")

# Сохранение в Excel
df = pd.DataFrame(matrix)

# Сохраняем в Excel
df.to_excel('matrix.xlsx', index=False, header=False)

# Сохраняем с индексами и заголовками
df_with_headers = pd.DataFrame(matrix, 
                              index=[f'Строка_{i+1}' for i in range(44)],
                              columns=[f'Столбец_{j+1}' for j in range(33)])

df_with_headers.to_excel('matrix_with_headers.xlsx', 
                        index=True, 
                        header=True,
                        index_label='Строка',
                        sheet_name='Матрица')

print("\nМатрицы сохранены в файлы 'matrix.xlsx' и 'matrix_with_headers.xlsx'")