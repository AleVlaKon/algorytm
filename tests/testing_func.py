def is_symmetric(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if matrix[i][j] != matrix[j][i]:
                return False
    return True