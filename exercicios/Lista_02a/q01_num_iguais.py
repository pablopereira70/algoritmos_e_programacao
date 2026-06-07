"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))
    numero_3 = int(input('Digite o terceiro número: '))

    quantidade_numeros_iguais = obter_quantidade_de_numeros_iguais(numero_1, numero_2, numero_3)

    if quantidade_numeros_iguais == 3:
        print('Todos os números são iguais')
    elif quantidade_numeros_iguais == 2:
        print('Dois números são iguais')
    else:
        print('Nenhum número é igual')


def obter_quantidade_de_numeros_iguais(n1, n2, n3):
    quantidade = 0
    if n1 == n2 and n1 == n3:
        quantidade += 3
    elif n1 != n2 and n1 != n3 and n2 != n3:
        quantidade += 0
    else:
        quantidade += 2
    return quantidade


main()