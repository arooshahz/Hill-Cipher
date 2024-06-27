def get_minor(matrix, row, col):
    minor = []
    for i in range(len(matrix)):
        if i != row:
            new_row = []
            for j in range(len(matrix[i])):
                if j != col:
                    new_row.append(matrix[i][j])
            minor.append(new_row)
    return minor


def LaplaceExpansion(matrix):
    if len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for i in range(len(matrix[0])):
        minor = get_minor(matrix, 0, i)
        det += ((-1) ** i) * matrix[0][i] * LaplaceExpansion(minor)
    return det


matrix = [[1, 2, 3],
          [0, 5, 6],
          [0, 8, 9]]

print(f'Determinant: {LaplaceExpansion(matrix)}')
