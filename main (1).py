import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Criar ou Carregar Dados
dados = {
    'idade': [25, 30, 45, 35, 22, 54, 40, 28, 51, 38],
    'salario': [5000, 6200, 11000, 7500, 4200, 15000, 9000, 5800, 13000, 8200],
    'fez_compra': [0, 0, 1, 1, 0, 1, 1, 0, 1, 1]
}
df = pd.DataFrame(dados)

# 2. Análise Exploratória e Limpeza
print("--- Primeiras Linhas ---")
print(df.head())

print("\n--- Estatísticas Descritivas ---")
print(df.describe())

# Verificar e tratar valores nulos (se existirem)
df = df.fillna(df.mean())

# 3. Visualização de Dados
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='idade', y='salario', hue='fez_compra', palette='viridis', s=100)
plt.title('Relação entre Idade, Salário e Decisão de Compra')
plt.xlabel('Idade')
plt.ylabel('Salário (R$)')
plt.grid(True)
plt.show()

# 4. Divisão em Treino e Teste
X = df[['idade', 'salario']] # Recursos (Features)
y = df['fez_compra']         # Alvo (Target)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 5. Treinamento do Modelo de Machine Learning
modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_train, y_train)

# 6. Avaliação de Desempenho
predicoes = modelo.predict(X_test)
acuracia = accuracy_score(y_test, predicoes)

print(f"\nAcurácia do Modelo: {acuracia * 100:.2f}%")
print("\nRelatório de Classificação:")
print(classification_report(y_test, predicoes))