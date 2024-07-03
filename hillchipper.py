from jordan import jordan


def char_to_num(char):
    return ord(char) - ord('A')


def num_to_char(num):
    return chr(num + ord('A'))


def text_to_matrices(text):
    text = text.upper()

    if len(text) % 2 != 0:
        text += 'X'

    matrices = []

    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i + 1]
        num1 = char_to_num(char1)
        num2 = char_to_num(char2)

        matrix = [[num1], [num2]]
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
    result = [
        [key_matrix[0][0] * text_matrix[0][0] + key_matrix[0][1] * text_matrix[1][0]],
        [key_matrix[1][0] * text_matrix[0][0] + key_matrix[1][1] * text_matrix[1][0]]
    ]
    return result


def mod_26(matrix):
    return [[element % 26] for row in matrix for element in row]


def matrix_inverse(matrix):
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]

    determinant = int(jordan(matrix))
    det_inv = pow(determinant, -1, 26)  # Calculate modular multiplicative inverse

    adjugate = [[d, -b], [-c, a]]

    inverse_matrix = [[adjugate[0][0] * det_inv % 26, adjugate[0][1] * det_inv % 26],
                      [adjugate[1][0] * det_inv % 26, adjugate[1][1] * det_inv % 26]]

    return inverse_matrix


def hill_cipher_encrypt(text, key_matrix):
    matrices = text_to_matrices(text)

    cipher_matrices = []
    for text_matrix in matrices:
        product = multiply_matrices(key_matrix, text_matrix)
        cipher_matrix = mod_26(product)
        cipher_matrices.append(cipher_matrix)

    cipher_text = matrices_to_text(cipher_matrices)
    return cipher_text


def hill_cipher_decrypt(text, key_matrix):
    matrices = text_to_matrices(text)
    key_matrix_inv = matrix_inverse(key_matrix)
    cipher_matrices = []
    for text_matrix in matrices:
        product = multiply_matrices(key_matrix_inv, text_matrix)
        cipher_matrix = mod_26(product)
        cipher_matrices.append(cipher_matrix)

    cipher_text = matrices_to_text(cipher_matrices)

    return cipher_text


text = "hello"
key_matrix = [[3, 3], [2, 5]]
n = len(text)

cipher_text = hill_cipher_encrypt(text, key_matrix)
print("encoded text : ", cipher_text)

cipher_text = hill_cipher_decrypt(cipher_text, key_matrix)
if cipher_text[-1] == 'X' and n % 2 == 1:
    cipher_text = cipher_text[:-1]
print("decoded text : ", cipher_text)
