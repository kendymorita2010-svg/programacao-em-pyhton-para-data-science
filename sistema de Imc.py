def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media


def verificar_situacao(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"


def sistema_media():
    nome = input("Digite o nome do aluno: ")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = calcular_media(nota1, nota2, nota3)
    situacao = verificar_situacao(media)

    print("\n--- RESULTADO ---")
    print("Aluno:", nome)
    print("Média:", round(media, 2))
    print("Situação:", situacao)


sistema_media()