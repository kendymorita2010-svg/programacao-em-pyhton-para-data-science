import streamlit as st
import plotly.express as px
from main import carregar_dados, treinar_modelo_legendarios

st.set_page_config(page_title="Pokémon Data Dashboard", layout="wide")

st.title("⚡ Pokémon Data Dashboard & Trios Lendários")

df = carregar_dados('pokemon.csv')

# --- FILTROS ---
st.sidebar.header("Filtros")
somente_lendarios = st.sidebar.checkbox("Mostrar Apenas Lendários", value=False)

if somente_lendarios:
    df_exibicao = df[df['Legendary'] == True]
else:
    df_exibicao = df.copy()

# --- MÉTRICAS PRINCIPAIS ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Exibido", len(df_exibicao))
col2.metric("Média Total Stats", f"{df_exibicao['Total_Stats'].mean():.1f}")
col3.metric("Lendários na Base", len(df[df['Legendary'] == True]))

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["Comparativo de Trios", "Ataque vs Velocidade", "Modelo Preditivo"])

with tab1:
    st.subheader("Média de Status dos Trios Lendários")
    df_trios = df[df['Trio'] != 'Nenhum']
    fig_trios = px.bar(
        df_trios, 
        x='Name', 
        y='Total_Stats', 
        color='Trio',
        text='Total_Stats',
        title="Comparação Individual dos Pokémon nos Trios"
    )
    st.plotly_chart(fig_trios, use_container_width=True)

with tab2:
    st.subheader("Relação Ataque vs Velocidade")
    fig_scatter = px.scatter(
        df_exibicao, 
        x='Attack', 
        y='Speed', 
        color='Trio', 
        hover_name='Name', 
        size='Total_Stats'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with tab3:
    st.subheader("Importância das Variáveis na Predição de Lendários")
    importancias = treinar_modelo_legendarios(df)
    st.bar_chart(importancias.set_index('Atributo'))