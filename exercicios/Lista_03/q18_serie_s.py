"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que calcula os termos da série S = 1/1 + 2/2 + 3/3 + 4/4 + ... + N/N, onde N é um número inteiro fornecido pelo usuário.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    n = int(input('Digite o número de termos: '))

    sub = 0
    for i in range(1, n + 1):
        s = i / (i - sub)
        sub += 1
        print(s)


main()