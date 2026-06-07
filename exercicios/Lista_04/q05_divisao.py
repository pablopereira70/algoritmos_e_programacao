"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    x = obter_inteiro("Digite um número inteiro: ")
    n = obter_inteiro("Digite um número inteiro: ")

    divisoes_sucessivas(x, n)


def divisoes_sucessivas(x, n):
    n1 = x
    n2 = n
    contador = 1

    while n2 > 1:
        div = n1 / n2
        print(f"{contador}º divisão: {div}")
        n1 = div
        n2 -= 1
        contador += 1


main()