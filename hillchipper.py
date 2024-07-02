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


def hill_cipher_encrypt(text, key_matrix):
    matrices = text_to_matrices(text)

    cipher_matrices = []
    for text_matrix in matrices:
        product = multiply_matrices(key_matrix, text_matrix)
        cipher_matrix = mod_26(product)
        cipher_matrices.append(cipher_matrix)

    cipher_text = matrices_to_text(cipher_matrices)
    return cipher_text



text = "HELP"
key_matrix = [[3, 3], [2, 5]]

cipher_text = hill_cipher_encrypt(text, key_matrix)
print("encoded text : ", cipher_text)

