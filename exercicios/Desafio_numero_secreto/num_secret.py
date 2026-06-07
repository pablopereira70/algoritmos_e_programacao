"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

import random

def main():
    numero_secreto = random.randint(1, 100)
    contador = 10
    pontuacao = 100
    tentativas = 1
    pare = False

    while contador > 0:
        palpite = obter_palpite(tentativas)
        pare = analisar_palpite(palpite, numero_secreto)
         
        if pare == True:
            break

        contador -= 1
        tentativas += 1
        pontuacao -= 10

    print(f"Número secreto: {numero_secreto}")
    print(f"Pontuação:      {pontuacao}")
    print(f"Tentativas:     {tentativas}")


def obter_palpite(t):
    print(f"{t}º tentativa")
    num = int(input("Digite o seu palpite: "))
    return num


def analisar_palpite(n,s):
    if n == s:
        print("PARABÉNS!!! você acertou")
        return True
    elif n > s:
        print("ERROU!!!!")
        print("O número secreto é menor")
    else:
        print("ERROU!!!!")
        print("O número secreto é maior")


main()