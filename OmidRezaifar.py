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


def OmidRezaifar(matrix):
    if len(matrix[0]) == 1:
        return matrix[0][0]
    if len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    n = len(matrix[0])
    M = [[0, 0],
         [0, 0]]
    M[0][0] = OmidRezaifar(get_minor(matrix, 0, 0))
    M[0][1] = OmidRezaifar(get_minor(matrix, 0, n - 1))
    M[1][0] = OmidRezaifar(get_minor(matrix, n - 1, 0))
    M[1][1] = OmidRezaifar(get_minor(matrix, n - 1, n - 1))
    m = OmidRezaifar(get_minor(get_minor(matrix, n - 1, n - 1), 0, 0))
    det = (M[0][0] * M[1][1] - M[0][1] * M[1][0]) / m
    return det


matrixA = [[5, 9, 7],
           [8, 12, 13],
           [-1, 15, 4]]
print(f'Determinant A: {OmidRezaifar(matrixA)}')

matrixB = [[10, 1, 3, -7],
           [5, 4, 1, 12],
           [0, 2, 10, 1],
           [4, 3, 20, 11]]
print(f'Determinant B: {OmidRezaifar(matrixB)}')
