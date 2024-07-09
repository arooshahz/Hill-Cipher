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


def hill_cipher_encrypt(text, key_matrix):
    if jordan(key_matrix) == 0:
        return "NO_VALID_KEY"
    n = len(key_matrix)
    matrices = text_to_matrices(text, n)

    cipher_matrices = []
    for text_matrix in matrices:
        product = multiply_matrices(key_matrix, text_matrix)
        cipher_matrix = mod_26(product)
        cipher_matrices.append(cipher_matrix)

    cipher_text = matrices_to_text(cipher_matrices)
    return cipher_text


n = int(input())
key_matrix = []
# print("Enter key matrix (each row separated by space):")
for i in range(n):
    row = list(map(int, input().split()))
    if len(row) != n:
        raise ValueError("Row length does not match n")
    key_matrix.append(row)

plaintext = input()
plaintext = plaintext.replace(" ", "_").upper()
cipher_text = hill_cipher_encrypt(plaintext, key_matrix)
print(cipher_text)