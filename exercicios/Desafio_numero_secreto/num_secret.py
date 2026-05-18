"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que implementa um jogo de adivinhação, onde o usuário tem 10 tentativas para adivinhar um número secreto entre 1 e 100. O programa fornece feedback se o palpite é maior ou menor que o número secreto e calcula a pontuação com base nas tentativas restantes.
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