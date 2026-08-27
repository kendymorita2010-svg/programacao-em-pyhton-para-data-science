import numpy as np





temperaturas = np.array([22, 25, 19, 30, 28, 21, 18, 33])


# Filtre apenas as temperaturas acima de 24 graus.


acima  =  np.array([n for n in temperaturas if n > 24])
print(acima)


# Calcule quantas temperaturas ficaram acima da média.


media  =  np.mean(temperaturas)
print(media)


lista_acima =  np.array([z for z in temperaturas if z > media])
print(lista_acima)



# Crie um novo array com os valores normalizados 


novo =  [t for t in temperaturas if t < media]


# (subtraia a média e divida pelo desvio padrão).


desv = round(np.std((novo)),2)
print(desv)
sub =  novo - desv
print(np.array(sub))