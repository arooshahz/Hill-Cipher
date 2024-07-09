def get_minor(matrix, row, col):
    return [
        [matrix[i][j] for j in range(len(matrix)) if j != col]
        for i in range(len(matrix)) if i != row
    ]


def LaplaceExpansion(matrix, memo={}):
    key = tuple(map(tuple, matrix))
    if key in memo:
        return memo[key]

    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for i in range(len(matrix[0])):
        minor = get_minor(matrix, 0, i)
        det += ((-1) ** i) * matrix[0][i] * LaplaceExpansion(minor, memo)

    memo[key] = det
    return det

try:
    n = int(input().strip())
    matrix = []

    for _ in range(n):
        row = list(map(float, input().strip().split()))
        if len(row) != n:
            raise ValueError(f"Each row must contain {n} elements.")
        matrix.append(row)

    det = LaplaceExpansion(matrix)

    print(int(det))

except ValueError as e:
    print("Invalid input:", str(e))
