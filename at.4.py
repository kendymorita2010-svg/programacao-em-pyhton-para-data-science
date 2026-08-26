# 4 - MANIPULE AS TEMPERATURAS

import numpy as np

temperaturas = np.array([22, 25, 19, 30, 28, 21, 18, 33])

# Filtre apenas as temperaturas acima de 24 graus
acima_24 = temperaturas[temperaturas > 24]

print("Temperaturas acima de 24 graus:", acima_24)

# Calcule a média
media = np.mean(temperaturas)

# Calcule quantas temperaturas ficaram acima da média
quantidade_acima_media = np.sum(temperaturas > media)

print("Média:", media)
print("Quantidade acima da média:", quantidade_acima_media)

# Crie um novo array com os valores normalizados
# (valor - média) / desvio padrão
desvio_padrao = np.std(temperaturas)

temperaturas_normalizadas = (temperaturas - media) / desvio_padrao

print("Temperaturas normalizadas:", temperaturas_normalizadas)