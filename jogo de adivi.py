# JOGO DA ADIVINHAÇÃO

import random

numero_secreto = random.randint(1, 100)


def verificar_palpite(palpite):
    if palpite == numero_secreto:
        return "acertou"
    elif palpite < numero_secreto:
        return "maior"
    else:
        return "menor"


def iniciar_jogo():
    tentativas = 0

    print("=== JOGO DA ADIVINHAÇÃO ===")
    print("Tente adivinhar um número de 1 a 100!")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        resultado = verificar_palpite(palpite)

        if resultado == "acertou":
            print("Parabéns! Você acertou!")
            print("Número de tentativas:", tentativas)
            break

        elif resultado == "maior":
            print("O número secreto é MAIOR.")

        else:
            print("O número secreto é MENOR.")


iniciar_jogo()