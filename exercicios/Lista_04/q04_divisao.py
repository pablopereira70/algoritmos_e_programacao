"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    num = obter_inteiro("Digite um número inteiro: ")

    ultima_divisao = obter_ultima_divisao(num)

    print(f"última divisão efetuada: {ultima_divisao}")


def obter_ultima_divisao(n):
    div = n
    ult_div = None

    while True:
        div /= 2

        if div < 1:
            return ult_div
        
        ult_div = div


main()