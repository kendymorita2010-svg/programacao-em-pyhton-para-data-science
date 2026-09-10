import numpy as np
from sklearn.linear_model import LinearRegression

dias = np.array([10, 20, 30, 40, 50]).reshape(-1, 1)
altura_cm = np.array([5, 12, 18, 25, 30])

modelo3 = LinearRegression().fit(dias, altura_cm)
print(f"Coef: {modelo3.coef_[0]:.3f}, Intercepto: {modelo3.intercept_:.3f}")
print(f"Previsão para 35 dias: {modelo3.predict([[35]])[0]:.2f}")