
def get_minor(matrix, row, col):
    return [
        [matrix[i][j] for j in range(len(matrix)) if j != col]
        for i in range(len(matrix)) if i != row
    ]


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


def char_to_num(char):
    if char == '_':
        return 26
    return ord(char) - ord('A')


def num_to_char(num):
    if num == 26:
        return '_'
    return chr(num + ord('A'))


def text_to_matrices(text, n):
    text = text.upper()

    if len(text) % n != 0:
        text += '_' * (n - len(text) % n)

    matrices = []

    for i in range(0, len(text), n):
        matrix = []
        for j in range(n):
            matrix.append([char_to_num(text[i + j])])
        matrices.append(matrix)

    return matrices


def matrices_to_text(matrices):
    text = ""
    for matrix in matrices:
        for row in matrix:
            for num in row:
                text += num_to_char(num)
    return text


def multiply_matrices(key_matrix, text_matrix):
    key_rows = len(key_matrix)
    key_cols = len(key_matrix[0])
    text_cols = len(text_matrix[0])

    result = [[0] * text_cols for _ in range(key_rows)]

    for i in range(key_rows):
        for j in range(text_cols):
            for k in range(key_cols):
                result[i][j] += key_matrix[i][k] * text_matrix[k][j]

    return result


def mod_26(matrix):
    return [[element % 27] for row in matrix for element in row]


def mod_inverse(det, m):
    for i in range(1, m):
        if (det * i) % m == 1:
            return i
    return None


def matrix_inverse(matrix):
    n = len(matrix)
    det = int(jordan(matrix))
    det_inv = pow(det, -1, 27)

    if det == 0:
        raise ValueError("The matrix is not invertible.")

    adj = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            minor = get_minor(matrix, i, j)
            adj[j][i] = ((-1) ** (i + j)) * round(jordan(minor))

    inverse_matrix = [[((adj[i][j] * det_inv) % 27) for j in range(n)] for i in range(n)]

    return inverse_matrix


def hill_cipher_decrypt(text, key_matrix):
    if jordan(key_matrix) == 0:
        return "NO_VALID_KEY"
    n = len(key_matrix)

    matrices = text_to_matrices(text, n)

    key_matrix_inv = matrix_inverse(key_matrix)

    cipher_matrices = []
    for text_matrix in matrices:
        product = multiply_matrices(key_matrix_inv, text_matrix)
        cipher_matrix = mod_26(product)
        cipher_matrices.append(cipher_matrix)

    cipher_text = matrices_to_text(cipher_matrices)

    return cipher_text


n = int(input())
key_matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    if len(row) != n:
        raise ValueError("Row length does not match n")
    key_matrix.append(row)

plaintext = input()
plaintext = plaintext.replace(" ", "_").upper()
cipher_text = hill_cipher_decrypt(plaintext, key_matrix)
if cipher_text[-1] == '_':
    cipher_text = cipher_text[:-1]
print(cipher_text)