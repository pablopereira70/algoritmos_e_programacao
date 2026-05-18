"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais 
Descrição: Programa que recebe cinco números inteiros, calcula a média desses números, e exibe os números que são maiores do que a média calculada.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    num1 = int(input('Digite um número inteiro qualquer: '))
    num2 = int(input('Digite um número inteiro qualquer: '))
    num3 = int(input('Digite um número inteiro qualquer: '))
    num4 = int(input('Digite um número inteiro qualquer: '))
    num5 = int(input('Digite um número inteiro qualquer: '))

    media = calcular_media(num1, num2, num3, num4, num5)

    escrever_nums_maior_media(media, num1, num2, num3, num4, num5)


def calcular_media(n1, n2, n3, n4, n5):
    return (n1 + n2 + n3 + n4 + n5) / 5


def escrever_nums_maior_media(u, n1, n2, n3, n4, n5):
    print('Os números maiores que a média são:')
    if n1 > u:
        print(n1)
    if n2 > u:
        print(n2)
    if n3 > u:
        print(n3)
    if n4 > u:
        print(n4)
    if n5 > u:
        print(n5)


main()