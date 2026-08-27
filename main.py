import pandas as pd

# ==========================================
# 1 - Lendo o arquivo CSV
# ==========================================
dados = pd.read_csv("dados.csv")

# ==========================================
# 2 - Criando um DataFrame
# ==========================================
df = pd.DataFrame(dados)

print("DATAFRAME:")
print(df)


# ==========================================
# 3 - Calculando a média de idade
# ==========================================
media_idade = df["Idade"].mean()

print("\nMÉDIA DE IDADE:")
print(media_idade)


# ==========================================
# 4 - Calculando a mediana de idade
# ==========================================
mediana_idade = df["Idade"].median()

print("\nMEDIANA DE IDADE:")
print(mediana_idade)


# ==========================================
# 5 - Buscando os dados da Maria
# ==========================================
maria = df[df["Nome"] == "Maria"]

print("\nDADOS DA MARIA:")
print(maria)


# ==========================================
# 6 - Informações técnicas do CSV
# ==========================================
print("\nINFORMAÇÕES TÉCNICAS:")
print(df.info())


# ==========================================
# 7 - Descrição básica (estatística)
# ==========================================
print("\nDESCRIÇÃO ESTATÍSTICA:")
print(df.describe())


# ==========================================
# 8 - Agregação com groupby()
# ==========================================
grupo_cidade = df.groupby("Cidade")["Idade"].agg(
    ["count", "mean", "min", "max"]
)

print("\nAGREGAÇÃO POR CIDADE:")
print(grupo_cidade)