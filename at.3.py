import numpy as np

# 3 - EXPLORE A DOCUMENTAÇÃO
# https://numpy.org/doc/stable/

vendas = np.array([120, 90, 150, 80, 200, 110, 50, 300])

# Filtre apenas as vendas maiores que 100
vendas_maiores_100 = vendas[vendas > 100]

print("Vendas maiores que 100:", vendas_maiores_100)

# Calcule quantas vendas ficaram abaixo da média
media = np.mean(vendas)
quantidade_abaixo_media = np.sum(vendas < media)

print("Média das vendas:", media)
print("Quantidade de vendas abaixo da média:", quantidade_abaixo_media)

# Crie um novo array dividindo cada valor pelo máximo
vendas_normalizadas = vendas / np.max(vendas)

print("Vendas divididas pelo máximo:", vendas_normalizadas)