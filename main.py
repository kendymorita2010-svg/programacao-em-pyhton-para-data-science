import requests
from bs4 import BeautifulSoup
import csv

URL = "https://gratuitos.netlify.app"

def extrair_cursos():
    resposta = requests.get(URL)
    resposta.raise_for_status()

    soup = BeautifulSoup(resposta.text, "html.parser")

    tabela = soup.find("table")
    if not tabela:
        print("Nenhuma tabela encontrada na página.")
        return []

    linhas = tabela.find_all("tr")

    # Cabeçalho
    cabecalho = [th.get_text(strip=True) for th in linhas[0].find_all(["th", "td"])]

    dados = []
    for linha in linhas[1:]:
        colunas = [td.get_text(strip=True) for td in linha.find_all("td")]
        if colunas:
            dados.append(dict(zip(cabecalho, colunas)))

    return dados


def salvar_csv(dados, nome_arquivo="cursos.csv"):
    if not dados:
        return
    with open(nome_arquivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=dados[0].keys())
        writer.writeheader()
        writer.writerows(dados)
    print(f"Arquivo salvo: {nome_arquivo}")


if __name__ == "__main__":
    cursos = extrair_cursos()
    for curso in cursos:
        print(curso)
    salvar_csv(cursos)