import statistics

# Listas de frequência
FREQUENCIA_1 = [1, 2, 3, 6, 4]
FREQUENCIA_2 = [1.5, 6.8, 9.7, 10.6]
FREQUENCIA_3 = [200, 300, 500, 700, 900, 400, 600]


def analisar_frequencia_1(dados):
    """Calcula média, mediana e moda da FREQUENCIA_1."""
    media = statistics.mean(dados)
    mediana = statistics.median(dados)
    moda = statistics.mode(dados)
    return media, mediana, moda


def analisar_frequencia_2(dados):
    """Calcula média, mediana e moda da FREQUENCIA_2."""
    media = statistics.mean(dados)
    mediana = statistics.median(dados)
    moda = statistics.mode(dados)
    return media, mediana, moda


def analisar_frequencia_3(dados):
    """Calcula média, mediana e moda da FREQUENCIA_3."""
    media = statistics.mean(dados)
    mediana = statistics.median(dados)
    moda = statistics.mode(dados)
    return media, mediana, moda


if __name__ == "__main__":
    for nome, dados, funcao in [
        ("FREQUENCIA_1", FREQUENCIA_1, analisar_frequencia_1),
        ("FREQUENCIA_2", FREQUENCIA_2, analisar_frequencia_2),
        ("FREQUENCIA_3", FREQUENCIA_3, analisar_frequencia_3),
    ]:
        media, mediana, moda = funcao(dados)
        print(f"--- {nome} ---")
        print(f"Média: {media}")
        print(f"Mediana: {mediana}")
        print(f"Moda: {moda}")
        print()