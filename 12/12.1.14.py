def diagonal_sum(matrix: list) -> int:
    n = len(matrix)
    result = 0

    for i in range(n):
        result += matrix[i][i]
        result += matrix[n - i - 1][i]

    if n % 2 == 1:
        middle = n // 2
        result -= matrix[middle][middle]
    
    return result


matrix = [[1, 2, 3],
          [6, 5, 4],
          [7, 8, 9]]
          
print(diagonal_sum(matrix))    # 1 + 5 + 9 + 3 + 7 = 25