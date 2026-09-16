import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

def carregar_dados(caminho_csv):
    """Lê, trata e categoriza os dados dos Pokémon."""
    df = pd.read_csv(caminho_csv)
    
    # Tratamento de nulos
    df['Type 2'] = df['Type 2'].fillna('None')
    
    # Criar novas variáveis
    df['Total_Stats'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
    
    # Classificação por Função (Role)
    condicoes = [
        (df['Speed'] >= 95),
        (df['Defense'] + df['Sp. Def'] >= 200)
    ]
    escolhas = ['Sweeper (Rápido)', 'Tank (Defensivo)']
    df['Role'] = np.select(condicoes, escolhas, default='Balanced')
    
    # Mapeamento de Trios Lendários
    aves_lendarias = ['Articuno', 'Zapdos', 'Moltres']
    feras_lendarias = ['Raikou', 'Entei', 'Suicune']
    trio_hoenn = ['Groudon', 'Kyogre', 'Rayquaza']
    
    df['Trio'] = 'Nenhum'
    df.loc[df['Name'].isin(aves_lendarias), 'Trio'] = 'Aves Lendárias (Kanto)'
    df.loc[df['Name'].isin(feras_lendarias), 'Trio'] = 'Feras Lendárias (Johto)'
    df.loc[df['Name'].isin(trio_hoenn), 'Trio'] = 'Criadores de Hoenn'
    
    return df

def treinar_modelo_legendarios(df):
    """Treina o modelo de Random Forest para prever Pokémon Lendários."""
    atributos = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
    X = df[atributos]
    y = df['Legendary']
    
    modelo = RandomForestClassifier(random_state=42)
    modelo.fit(X, y)
    
    df_importancia = pd.DataFrame({
        'Atributo': atributos,
        'Importância': modelo.feature_importances_
    }).sort_values(by='Importância', ascending=False)
    
    return df_importancia