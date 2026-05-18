"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que calcula os termos da série S = 1/1 - 1/2 + 1/3 - 1/4 + ... + 1/N, onde N é um número inteiro fornecido pelo usuário.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    n = int(input('Digite a quantidade de termos: '))

    for i in range(1, n + 1):
        s = 1 / i
        if i % 2 == 0:
            print(-s)
        else:
            print(s)


main()