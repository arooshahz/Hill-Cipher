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


def get_minor(matrix, row, col):
    return [
        [matrix[i][j] for j in range(len(matrix)) if j != col]
        for i in range(len(matrix)) if i != row
    ]


def OmidRezaifar(matrix):
    n = len(matrix)

    # Base cases
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    M = [0, 0, 0, 0]
    M[0] = OmidRezaifar(get_minor(matrix, 0, 0))
    M[1] = OmidRezaifar(get_minor(matrix, 0, n - 1))
    M[2] = OmidRezaifar(get_minor(matrix, n - 1, 0))
    M[3] = OmidRezaifar(get_minor(matrix, n - 1, n - 1))
    m = OmidRezaifar(get_minor(get_minor(matrix, n - 1, n - 1), 0, 0))

    if m != 0:
        det = (M[0] * M[3] - M[1] * M[2]) / m
    else:
        det = jordan(matrix)

    return det


try:
    n = int(input().strip())
    matrix = []

    for _ in range(n):
        row = list(map(float, input().strip().split()))
        if len(row) != n:
            raise ValueError(f"Each row must contain {n} elements.")
        matrix.append(row)

    det = OmidRezaifar(matrix)

    print(int(det))

except ValueError as e:
    print("Invalid input:", str(e))
