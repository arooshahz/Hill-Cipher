import tkinter as tk
from tkinter import ttk, messagebox

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

def OmidRezaifar(matrix, steps=None):
    if steps is None:
        steps = []
    if len(matrix[0]) == 1:
        steps.append(f'Returning single element: {matrix[0][0]}')
        return matrix[0][0]
    if len(matrix[0]) == 2:
        result = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        steps.append(f'Base case 2x2: {matrix[0][0]}*{matrix[1][1]} - {matrix[0][1]}*{matrix[1][0]} = {result}')
        return result
    n = len(matrix[0])
    M = [[0, 0], [0, 0]]
    M[0][0] = OmidRezaifar(get_minor(matrix, 0, 0), steps)
    M[0][1] = OmidRezaifar(get_minor(matrix, 0, n - 1), steps)
    M[1][0] = OmidRezaifar(get_minor(matrix, n - 1, 0), steps)
    M[1][1] = OmidRezaifar(get_minor(matrix, n - 1, n - 1), steps)
    m = OmidRezaifar(get_minor(get_minor(matrix, n - 1, n - 1), 0, 0), steps)
    det = (M[0][0] * M[1][1] - M[0][1] * M[1][0]) / m
    steps.append(f'Calculating determinant: ({M[0][0]} * {M[1][1]} - {M[0][1]} * {M[1][0]}) / {m} = {det}')
    return det

def LaplaceExpansion(matrix, steps=None):
    if steps is None:
        steps = []
    if len(matrix[0]) == 2:
        result = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        steps.append(f'Base case 2x2: {matrix[0][0]}*{matrix[1][1]} - {matrix[0][1]}*{matrix[1][0]} = {result}')
        return result
    det = 0
    for i in range(len(matrix[0])):
        minor = get_minor(matrix, 0, i)
        cofactor = ((-1) ** i) * matrix[0][i]
        minor_det = LaplaceExpansion(minor, steps)
        det += cofactor * minor_det
        steps.append(f'Adding cofactor: {cofactor} * det(minor) = {cofactor} * {minor_det}')
    steps.append(f'Final determinant: {det}')
    return det

def jordan(matrix, steps=None):
    if steps is None:
        steps = []
    n = len(matrix)
    A = [row[:] for row in matrix]
    det = 1

    for i in range(n):
        if A[i][i] == 0:
            for j in range(i + 1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    det *= -1
                    steps.append(f'Swapping rows {i} and {j}, det *= -1')
                    break
            else:
                steps.append(f'Column {i} is all zeros, determinant is 0')
                return 0

        det *= A[i][i]
        steps.append(f'Multiplying det by A[{i}][{i}] = {A[i][i]}')
        for k in range(i + 1, n):
            A[i][k] /= A[i][i]
        A[i][i] = 1

        for j in range(i + 1, n):
            factor = A[j][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            steps.append(f'Eliminating A[{j}][{i}] using row {i}')

    steps.append(f'Final determinant: {det}')
    return det

def calculate_determinant():
    try:
        n = int(entry_n.get())
        matrix = []
        for i in range(n):
            row = [float(entries[i][j].get()) for j in range(n)]
            matrix.append(row)
        
        method = method_combobox.get()
        steps = []

        if method == "Jordan":
            det = jordan(matrix, steps)
        elif method == "Laplace":
            det = LaplaceExpansion(matrix, steps)
        elif method == "OmidRezaifar":
            det = OmidRezaifar(matrix, steps)
        else:
            messagebox.showerror("Error", "Please select a valid method")
            return

        text_steps.config(state=tk.NORMAL)
        text_steps.delete(1.0, tk.END)
        text_steps.insert(tk.END, "\n".join(steps))
        text_steps.config(state=tk.DISABLED)

        messagebox.showinfo("Determinant Results", f"{method} Method: {det}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def create_matrix_entries():
    try:
        n = int(entry_n.get())
        for widget in frame_matrix.winfo_children():
            widget.destroy()
        
        global entries
        entries = []
        for i in range(n):
            row_entries = []
            for j in range(n):
                entry = ttk.Entry(frame_matrix, width=5)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            entries.append(row_entries)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for n")

app = tk.Tk()
app.title("Matrix Determinant Calculator")
app.configure(bg='#1e1e1e')

style = ttk.Style()
style.theme_use('clam')

style.configure('TLabel', background='#1e1e1e', foreground='#ffffff')
style.configure('TButton', background='#0078d7', foreground='#ffffff', borderwidth=0, focuscolor='#0078d7')
style.configure('TEntry', fieldbackground='#333333', foreground='#ffffff', insertcolor='#ffffff')
style.configure('TCombobox', fieldbackground='#333333', background='#333333', foreground='#ffffff', arrowcolor='#ffffff')

frame_input = ttk.Frame(app)
frame_input.pack(pady=10)

label_n = ttk.Label(frame_input, text="Enter the size of the matrix (n):")
label_n.grid(row=0, column=0, padx=5, pady=5)

entry_n = ttk.Entry(frame_input, width=5)
entry_n.grid(row=0, column=1, padx=5, pady=5)

button_create = ttk.Button(frame_input, text="Create Matrix", command=create_matrix_entries)
button_create.grid(row=0, column=2, padx=5, pady=5)

frame_matrix = ttk.Frame(app)
frame_matrix.pack(pady=10)

method_combobox = ttk.Combobox(app, values=["Jordan", "Laplace", "OmidRezaifar"])
method_combobox.set("Select Method")
method_combobox.pack(pady=10)

button_calculate = ttk.Button(app, text="Calculate Determinant", command=calculate_determinant)
button_calculate.pack(pady=10)

text_steps = tk.Text(app, height=15, width=50, state=tk.DISABLED, bg='#1e1e1e', fg='#ffffff')
text_steps.pack(pady=10)

app.mainloop()
