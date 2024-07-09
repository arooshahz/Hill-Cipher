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


def floor(x):
    return int(x // 1) if x >= 0 else int(x // 1) - 1



try:
    n = int(input().strip())
    matrix = []

    for _ in range(n):
        row = list(map(float, input().strip().split()))
        if len(row) != n:
            raise ValueError(f"Each row must contain {n} elements.")
        matrix.append(row)

    det = jordan(matrix)

    print(int(det))

except ValueError as e:
    print("Invalid input:", str(e))



