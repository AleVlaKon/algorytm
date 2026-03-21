def is_symmetric(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


matrix = [[0, 1, 2],
          [1, 2, 3],
          [2, 3, 4]]

print(is_symmetric(matrix))

matrix = [[1]]

print(is_symmetric(matrix))

matrix = [[-10, 1, 6],
         [1, 5, -3],
         [6, -3, 3]]

print(is_symmetric(matrix))

matrix = [[1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1]]

print(is_symmetric(matrix))

matrix = [[1, 2],
          [3, 4]]

print(is_symmetric(matrix))