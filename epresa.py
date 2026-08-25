import statistics


# =========================
# SALÁRIOS DAS EMPRESAS
# =========================

empresa1 = [2500, 2800, 3000, 9500, 12000]
empresa2 = [5000, 5200, 5300, 5400, 5500]
empresa3 = [1000, 2000, 8000, 15000, 20000]
empresa4 = [3500, 4000, 4200, 4300, 6000]
empresa5 = [1200, 1500, 1800, 2500, 10000]


# =========================
# FUNÇÃO DE ANÁLISE
# =========================

def analisar_salarios(nome, salarios):

    media = statistics.mean(salarios)
    mediana = statistics.median(salarios)
    desvio = statistics.pstdev(salarios)
    variancia = statistics.pvariance(salarios)
    amplitude = max(salarios) - min(salarios)

    try:
        moda = statistics.mode(salarios)
    except statistics.StatisticsError:
        moda = "Não existe"

    print(f"\n{'=' * 45}")
    print(f"{nome:^45}")
    print(f"{'=' * 45}")

    print(f"{'Média:':<20} R$ {media:>10.2f}")
    print(f"{'Mediana:':<20} R$ {mediana:>10.2f}")
    print(f"{'Moda:':<20} R$ {str(moda):>10}")
    print(f"{'Desvio padrão:':<20} R$ {desvio:>10.2f}")
    print(f"{'Variância:':<20} {variancia:>15.2f}")
    print(f"{'Amplitude:':<20} R$ {amplitude:>10.2f}")


# =========================
# DADOS
# =========================

empresas = {
    "EMPRESA 1": empresa1,
    "EMPRESA 2": empresa2,
    "EMPRESA 3": empresa3,
    "EMPRESA 4": empresa4,
    "EMPRESA 5": empresa5
}


# =========================
# ANÁLISE
# =========================

for nome, salarios in empresas.items():
    analisar_salarios(nome, salarios)


# =========================
# CONCLUSÃO
# =========================

print(f"\n{'=' * 45}")
print(f"{'CONCLUSÃO':^45}")
print(f"{'=' * 45}")

print("A Empresa 2 é a melhor escolha.")
print("Ela apresenta salários mais próximos entre si,")
print("com menor variação e maior estabilidade salarial.")