"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que lê um número inteiro N e depois fica solicitando ao usuário que digite um número inteiro, até que o número digitado seja igual a N.
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