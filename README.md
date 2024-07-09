# Determinant Calculation and Hill Cipher Encoding/Decoding

This project provides an implementation for calculating the determinant of a matrix using three different methods: Jordan, Laplace, and Omid Rezai. Additionally, it includes encoding and decoding functionality using the Hill cipher.
Table of Contents



## Introduction

This project is designed to provide a comprehensive approach to determinant calculation and encryption. The determinant of a matrix is computed using three different methods, ensuring a robust understanding of linear algebra concepts. Additionally, the Hill cipher, a polygraphic substitution cipher, is used for encoding and decoding messages, showcasing an application of matrix operations in cryptography.
Methods

![image](https://github.com/arooshahz/Hill-Cipher/assets/136841773/0891bda0-20bc-4651-8776-f17513d61513)

## Determinant Methods
### Jordan Method

The Jordan method, also known as the Gaussian elimination, is a process of transforming a matrix into its reduced row echelon form to calculate its determinant.
### Laplace Method

The Laplace method, or cofactor expansion, is a recursive approach that breaks down the determinant calculation into smaller, manageable matrices.
### Omid Rezai Method

The Omid Rezai method is a unique approach to determinant calculation, based on Omid Rezai's research paper. This method offers an alternative perspective to traditional methods. For more details, you can refer to the original paper [here](https://drive.google.com/file/d/1E0uP1kMY8bdj5ABRt0voSop9mhUzpYlg/view). 


## Hill Cipher 

The Hill cipher is an encryption technique that uses linear algebra principles. It encodes and decodes messages by performing matrix multiplication.

### Encoding
The encoding process involves converting a plaintext message into a ciphertext by multiplying the plaintext vector with a key matrix.
![image](https://github.com/arooshahz/Hill-Cipher/assets/136841773/572f1994-15d0-4a22-b1e7-101da68a4dbf)

### Decoding
The decoding process involves reversing the encoding by multiplying the ciphertext vector with the inverse of the key matrix
The Jordan method is used to calculate the determinant in the Hill cipher due to its efficiency and accuracy compared to the other two methods
![image](https://github.com/arooshahz/Hill-Cipher/assets/136841773/6634634d-5465-44c9-bd5c-36cea35fd3ca)

