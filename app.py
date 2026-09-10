# # from sklearn.linear_model import LinearRegression
# from sklearn.neighbors import KNeighborsClassifier
# import numpy as np

# frutas_caracteristicas  =  np.array([[7,150],[8,170], [6,130], [9,180], [5,120]])
# classes_frutas  =  np.array([0,0,1,0,1])

# modelo = KNeighborsClassifier(n_neighbors=3)
# modelo.fit(frutas_caracteristicas, classes_frutas)


# nova_ = np.array([[4,120]])
# classifica = modelo.predict(nova_)[0]

# tipo = 'maça' if classifica == 0 else 'laranja'

# print(classifica)
















# horas_estudos  =  np.array([2,4,6,8,10]).reshape(-1,1)
# notas  =  np.array([4,4.5,5,7.5,8])

# modelo = LinearRegression()
# modelo.fit(horas_estudos, notas)

# hora_estudo = 7
# previsao = modelo.predict([[hora_estudo]])[0]
# print(previsao)
