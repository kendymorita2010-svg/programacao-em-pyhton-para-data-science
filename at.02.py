import numpy as np

# Criando duas matrizes 3x3
matriz1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matriz2 = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

# Calculando o produto das matrizes
produto = np.dot(matriz1, matriz2)

print("Matriz 1:")
print(matriz1)

print("\nMatriz 2:")
print(matriz2)

print("\nProduto:")
print(produto)