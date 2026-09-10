import numpy as np
from sklearn.linear_model import LinearRegression

fertilizante_kg = np.array([50, 100, 150, 200, 250]).reshape(-1, 1)
producao_ton = np.array([2.0, 3.5, 4.8, 5.5, 6.0])

modelo4 = LinearRegression().fit(fertilizante_kg, producao_ton)
print(f"Coef: {modelo4.coef_[0]:.3f}, Intercepto: {modelo4.intercept_:.3f}")
print(f"Previsão para 180kg: {modelo4.predict([[180]])[0]:.2f}")