"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    x = obter_inteiro("Digite um número inteiro: ")

    loop_infinito(x)

    print("Parabéns!! você saiu do loop")


def loop_infinito(x):
    n = obter_inteiro("Digite um número inteiro: ")
    while n != x:
        n = obter_inteiro("Digite um número inteiro: ")


main()