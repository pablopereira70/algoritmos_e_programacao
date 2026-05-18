"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que calcula os termos da série S = 1/1 + 3/2 + 5/3 + 7/4 + ... + (2N-1)/N, onde N é um número inteiro fornecido pelo usuário.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    n = int(input('Digite o número de termos: '))

    den = 1
    for i in range(1, n + 1):
        s = den / i
        den += 2
        print(s)


main()