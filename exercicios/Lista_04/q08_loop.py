"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que lê um número inteiro N, e depois lê N números inteiros.
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    x = obter_inteiro("Digite um número inteiro: ")

    loop_infinito(x)

    print('Parabéns!! você saiu do loop')


def loop_infinito(x):
    n1 = obter_inteiro("Digite um número inteiro: ")
    n2 = obter_inteiro("Digite um número inteiro: ")
    
    while n1 + n2 != x:
        n1 = n2
        n2 = obter_inteiro()


main()