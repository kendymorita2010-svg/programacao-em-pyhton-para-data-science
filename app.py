import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração global de estilo para o Matplotlib/Seaborn
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 10})

# -----------------------------------------------------------------------------
# 1. CONFIGURAÇÃO DA PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Dashboard Analítico - NBA Stats",
    page_icon="🏀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. CARREGAMENTO DOS DADOS (CACHE)
# -----------------------------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/NBA%20Player%20Stats%20-%20Basketball%20Reference/NBA%20Player%20Stats%20-%20Basketball%20Reference.csv")
    df = df.dropna(subset=['Points', 'Games', 'Pos'])
    df['Points_Per_Game'] = (df['Points'] / df['Games']).round(1)
    df['Rebounds_Per_Game'] = (df['Total Rebounds'] / df['Games']).round(1)
    df['Assists_Per_Game'] = (df['Assists'] / df['Games']).round(1)
    return df

try:
    df = load_data()
except Exception:
    st.warning("Carregando dados demonstrativos...")
    data = {
        'Player': ['LeBron James', 'Stephen Curry', 'Giannis Antetokounmpo', 'Kevin Durant', 'Nikola Jokic', 'Luka Doncic', 'Joel Embiid', 'Jayson Tatum'],
        'Pos': ['SF', 'PG', 'PF', 'PF', 'C', 'PG', 'C', 'SF'],
        'Tm': ['LAL', 'GSW', 'MIL', 'PHX', 'DEN', 'DAL', 'PHI', 'BOS'],
        'Age': [39, 36, 29, 35, 29, 25, 30, 26],
        'Games': [71, 74, 73, 75, 79, 70, 39, 74],
        'Points': [1822, 1956, 2222, 2032, 2085, 2370, 1353, 1987],
        'Total Rebounds': [518, 330, 841, 494, 971, 644, 429, 601],
        'Assists': [589, 379, 476, 378, 708, 686, 218, 364],
        'Season': [2024]*8
    }
    df = pd.DataFrame(data)
    df['Points_Per_Game'] = (df['Points'] / df['Games']).round(1)
    df['Rebounds_Per_Game'] = (df['Total Rebounds'] / df['Games']).round(1)
    df['Assists_Per_Game'] = (df['Assists'] / df['Games']).round(1)

# -----------------------------------------------------------------------------
# 3. BARRA LATERAL (FILTROS INTERATIVOS)
# -----------------------------------------------------------------------------
st.sidebar.header("🏀 Filtros do Dashboard")

# Filtro de Posição
posicoes_disponiveis = sorted(df['Pos'].unique().tolist())
posicoes_selecionadas = st.sidebar.multiselect(
    "Selecione a(s) Posição(ões):",
    options=posicoes_disponiveis,
    default=posicoes_disponiveis
)

# Filtro de Time
times_disponiveis = sorted(df['Tm'].unique().tolist())
times_selecionados = st.sidebar.multiselect(
    "Selecione o(s) Time(s):",
    options=times_disponiveis,
    default=times_disponiveis
)

# Filtro de Mínimo de Jogos
max_jogos = int(df['Games'].max())
min_jogos = st.sidebar.number_input(
    "Mínimo de Jogos Disputados:",
    min_value=1,
    max_value=max_jogos,
    value=10
)

# Filtro de Idade (Range Slider)
idade_min = int(df['Age'].min())
idade_max = int(df['Age'].max())
faixa_idade = st.sidebar.slider(
    "Faixa Etária:",
    min_value=idade_min,
    max_value=idade_max,
    value=(idade_min, idade_max)
)

# Filtro por Nome de Jogador
busca_nome = st.sidebar.text_input("Buscar Jogador por Nome:", "")

# Aplicação unificada dos filtros
df_filtrado = df[
    (df['Pos'].isin(posicoes_selecionadas)) &
    (df['Tm'].isin(times_selecionados)) &
    (df['Games'] >= min_jogos) &
    (df['Age'] >= faixa_idade[0]) &
    (df['Age'] <= faixa_idade[1])
]

if busca_nome:
    df_filtrado = df_filtrado[df_filtrado['Player'].str.contains(busca_nome, case=False, na=False)]

# -----------------------------------------------------------------------------
# 4. PAINEL PRINCIPAL (HEADER & METRICAS)
# -----------------------------------------------------------------------------
st.title("📊 Dashboard de Performance de Atletas - NBA")
st.markdown("Analise o desempenho individual e comparativo dos jogadores com base em filtros personalizados.")
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total de Jogadores Analisados", len(df_filtrado))
with col2:
    media_pts = df_filtrado['Points_Per_Game'].mean() if not df_filtrado.empty else 0
    st.metric("Média de Pts/Jogo", f"{media_pts:.1f}")
with col3:
    media_reb = df_filtrado['Rebounds_Per_Game'].mean() if not df_filtrado.empty else 0
    st.metric("Média de Reb/Jogo", f"{media_reb:.1f}")
with col4:
    media_ast = df_filtrado['Assists_Per_Game'].mean() if not df_filtrado.empty else 0
    st.metric("Média de Ast/Jogo", f"{media_ast:.1f}")

st.markdown("---")

# -----------------------------------------------------------------------------
# 5. VISUALIZAÇÕES DE DADOS (MATPLOTLIB / SEABORN)
# -----------------------------------------------------------------------------

if df_filtrado.empty:
    st.error("Nenhum jogador encontrado com os filtros selecionados.")
else:
    col_graf1, col_graf2 = st.columns(2)

    # Gráfico 1: Dispersão (Pontos/Jogo vs Assistências/Jogo por Posição)
    with col_graf1:
        st.subheader("🎯 Pontos vs. Assistências (por Posição)")
        fig1, ax1 = plt.subplots(figsize=(6, 4.5))
        
        sns.scatterplot(
            data=df_filtrado,
            x='Assists_Per_Game',
            y='Points_Per_Game',
            hue='Pos',
            size='Rebounds_Per_Game',
            sizes=(30, 200),
            alpha=0.7,
            ax=ax1
        )
        ax1.set_title("Pontos x Assistências (Tamanho = Rebotes)")
        ax1.set_xlabel("Assistências por Jogo")
        ax1.set_ylabel("Pontos por Jogo")
        ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        
        st.pyplot(fig1)

    # Gráfico 2: Top 10 Cestinhas
    with col_graf2:
        st.subheader("🏆 Top 10 Jogadores com Maior Média de Pontos")
        top_10_pts = df_filtrado.nlargest(10, 'Points_Per_Game').sort_values('Points_Per_Game', ascending=False)
        
        fig2, ax2 = plt.subplots(figsize=(6, 4.5))
        sns.barplot(
            data=top_10_pts,
            x='Points_Per_Game',
            y='Player',
            palette='Reds_r',
            ax=ax2
        )
        ax2.set_title("Top 10 Pontuadores")
        ax2.set_xlabel("Média de Pontos por Jogo")
        ax2.set_ylabel("Jogador")
        plt.tight_layout()
        
        st.pyplot(fig2)

    # Gráfico 3: Boxplot por Posição
    st.subheader("📈 Distribuição de Pontos por Posição")
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    
    sns.boxplot(
        data=df_filtrado,
        x='Pos',
        y='Points_Per_Game',
        palette='Set2',
        ax=ax3
    )
    sns.stripplot(
        data=df_filtrado,
        x='Pos',
        y='Points_Per_Game',
        color='black',
        alpha=0.3,
        jitter=0.2,
        ax=ax3
    )
    ax3.set_title("Distribuição da Média de Pontos por Posição")
    ax3.set_xlabel("Posição")
    ax3.set_ylabel("Pontos por Jogo")
    plt.tight_layout()
    
    st.pyplot(fig3)

    # -----------------------------------------------------------------------------
    # 6. TABELA DETALHADA E DOWNLOAD
    # -----------------------------------------------------------------------------
    with st.expander("📄 Ver Tabela de Dados Filtrados"):
        cols_exibicao = ['Player', 'Pos', 'Tm', 'Age', 'Games', 'Points_Per_Game', 'Rebounds_Per_Game', 'Assists_Per_Game']
        st.dataframe(df_filtrado[cols_exibicao].sort_values(by='Points_Per_Game', ascending=False), use_container_width=True)
        
        csv = df_filtrado[cols_exibicao].to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Baixar Dados Filtrados em CSV",
            data=csv,
            file_name="nba_filtered_stats.csv",
            mime="text/csv"
        )