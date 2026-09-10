import numpy as np
from sklearn.linear_model import LinearRegression

horas_estudo = np.array([2, 4, 6, 8, 10]).reshape(-1, 1)
notas = np.array([5.0, 6.5, 7.8, 8.5, 9.2])

modelo1 = LinearRegression().fit(horas_estudo, notas)
print(f"Coef: {modelo1.coef_[0]:.3f}, Intercepto: {modelo1.intercept_:.3f}")
print(f"Previsão para 7h de estudo: {modelo1.predict([[7]])[0]:.2f}")