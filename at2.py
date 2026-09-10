import numpy as np
from sklearn.linear_model import LinearRegression

temperaturas = np.array([15, 20, 25, 30, 35]).reshape(-1, 1)
consumo_kwh = np.array([120, 100, 90, 110, 150])

modelo2 = LinearRegression().fit(temperaturas, consumo_kwh)
print(f"Coef: {modelo2.coef_[0]:.3f}, Intercepto: {modelo2.intercept_:.3f}")
print(f"Previsão para 28°C: {modelo2.predict([[28]])[0]:.2f}")