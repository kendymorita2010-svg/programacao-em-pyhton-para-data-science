import numpy as np

# Crie um array 2D 5x5 com valores aleatórios entre 0 e 100
matriz = np.random.randint(0, 101, size=(5, 5))

print("Matriz:")
print(matriz)

# Calcule a média de cada linha
medias = np.mean(matriz, axis=1)

print("\nMédia de cada linha:")
print(medias)

# Encontre o maior e o menor valor da matriz
maior = np.max(matriz)
menor = np.min(matriz)

print("\nMaior valor:", maior)
print("Menor valor:", menor)