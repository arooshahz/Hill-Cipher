import tkinter as tk
from tkinter import messagebox


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

class HillCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hill Cipher")

        self.root.geometry("500x400")  
        self.root.configure(bg="#1c1c1c")
        self.create_widgets()

    def create_widgets(self):
        self.main_frame = tk.Frame(self.root, bg="#1c1c1c")
        self.main_frame.pack(padx=20, pady=20)

        self.text_label = tk.Label(self.main_frame, text="Enter text:", fg="white", bg="#1c1c1c")
        self.text_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.text_entry = tk.Entry(self.main_frame, width=50)
        self.text_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

        self.size_label = tk.Label(self.main_frame, text="Matrix size (n):", fg="white", bg="#1c1c1c")
        self.size_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.size_entry = tk.Entry(self.main_frame, width=5)
        self.size_entry.grid(row=1, column=1, sticky="w")

        self.create_matrix_button = tk.Button(self.main_frame, text="Create Matrix", command=self.create_matrix, bg="#007acc", fg="white")
        self.create_matrix_button.grid(row=1, column=1, padx=10, pady=10)

        self.matrix_frame = tk.Frame(self.main_frame, bg="#1c1c1c")
        self.matrix_frame.grid(row=2, column=0, columnspan=4, pady=10)

        self.matrix_entries = []
        self.encrypt_button = tk.Button(self.main_frame, text="Encrypt", command=self.encrypt, bg="#007acc", fg="white")
        self.encrypted_text_label = tk.Label(self.main_frame, text="Encrypted text:", fg="white", bg="#1c1c1c")
        self.encrypted_text_entry = tk.Entry(self.main_frame, width=50)

    def create_matrix(self):
        n = int(self.size_entry.get())
        self.clear_matrix()

        for i in range(n):
            row_entries = []
            for j in range(n):
                entry = tk.Entry(self.matrix_frame, width=5) 
                entry.grid(row=i, column=j, padx=5, pady=5)  
                row_entries.append(entry)
            self.matrix_entries.append(row_entries)

        self.encrypt_button.grid(row=3, column=1, columnspan=2, pady=10)
        self.encrypted_text_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.encrypted_text_entry.grid(row=4, column=1, columnspan=3, padx=10, pady=10)

    def clear_matrix(self):
        for row in self.matrix_entries:
            for entry in row:
                entry.grid_forget()
        self.matrix_entries = []

    def encrypt(self):
        n = int(self.size_entry.get())
        key_matrix = []

        for row_entries in self.matrix_entries:
            row = []
            for entry in row_entries:
                row.append(int(entry.get()))
            key_matrix.append(row)

        plaintext = self.text_entry.get().replace(" ", "_").upper()
        cipher_text = hill_cipher_encrypt(plaintext, key_matrix)

        if cipher_text == "NO_VALID_KEY":
            messagebox.showerror("Error", "The provided key matrix is not invertible.")
        else:
            self.encrypted_text_entry.delete(0, tk.END)
            self.encrypted_text_entry.insert(0, cipher_text)


root = tk.Tk()
app = HillCipherApp(root)
root.mainloop()
