def jordan(matrix):
    n = len(matrix)
    A = [row[:] for row in matrix] 
    det = 1

    for i in range(n):
        if A[i][i] == 0:
            for j in range(i + 1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i] 
                    det *= -1  
                    break
            else:
                return 0  

        det *= A[i][i]
        for k in range(i + 1, n):
            A[i][k] /= A[i][i]  
        A[i][i] = 1

        for j in range(i + 1, n):
            factor = A[j][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]

    return det

matrix = [
    [1, 2, 3],
    [0, 5, 6],
    [0, 8, 9]
]

det = jordan(matrix)
print(f'Determinant: {det}')
