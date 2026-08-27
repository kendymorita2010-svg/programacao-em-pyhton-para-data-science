import numpy as np

# Criando um array com 20 elementos
array = np.arange(1, 21)

# Primeiros 5 elementos
primeiros_5 = array[:5]

# Últimos 5 elementos
ultimos_5 = array[-5:]

# Elementos das posições 5 a 10
posicoes_5_a_10 = array[5:11]

print("Array:", array)
print("Primeiros 5:", primeiros_5)
print("Últimos 5:", ultimos_5)
print("Posições 5 a 10:", posicoes_5_a_10)