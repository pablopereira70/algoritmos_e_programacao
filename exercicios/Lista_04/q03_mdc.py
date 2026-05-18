"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que calcula o máximo divisor comum (MDC) de dois números inteiros utilizando o algoritmo de Euclides.
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    num_1 = obter_inteiro_nao_nulo("Digite um número inteiro não nulo: ")
    num_2 = obter_inteiro_nao_nulo("Digite um número inteiro não nulo: ")

    n1 = transformar_positivo(num_1)
    n2 = transformar_positivo(num_2)
    mdc = algoritmo_euclides(n1, n2)

    print(f"O mdc de {num_1} e {num_2} é: {mdc}")


def algoritmo_euclides(n1, n2):
    maior = obter_maior_numero(n1, n2)
    menor = obter_menor_numero(n1, n2)

    while True:
        resto = maior % menor

        if resto == 0:
            return menor
        
        maior = menor
        menor = resto


def obter_maior_numero(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


def obter_menor_numero(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2


main()