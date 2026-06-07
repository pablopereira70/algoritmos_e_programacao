"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    num_1 = obter_inteiro_nao_nulo("Digite um número inteiro não nulo: ")
    num_2 = obter_inteiro_nao_nulo("Digite um número inteiro não nulo: ")

    n1 = transformar_positivo(num_1)
    n2 = transformar_positivo(num_2)
    mmc = calcular_mmc(n1, n2)

    print(f"O mmc de {num_1} e {num_2} é: {mmc}")


def calcular_mmc(n1, n2):
    maior = obter_maior_numero(n1, n2)
    menor = obter_menor_numero(n1, n2)
    incremento = maior

    while True:

        if maior % menor == 0:
            return maior
        else:
            maior += incremento


def obter_maior_numero(n1, n2):
    maior = n1

    if n2 > maior:
        maior = n2

    return maior


def obter_menor_numero(n1, n2):
    menor = n1

    if n2 < menor:
        menor = n2

    return menor


main()