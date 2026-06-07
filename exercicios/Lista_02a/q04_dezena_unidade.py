"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    numero = int(input('Digite um número de dois dígitos: '))

    eh_igual = verifica_dezena_igual_unidade(numero)

    if eh_igual:
        print('O algarismo da dezena e da unidade são iguais')
    else:
        print('O algarismo da dezena e da unidade são diferentes')


def verifica_dezena_igual_unidade(numero):
    dezena = numero // 10
    unidade = numero % 10
    return dezena == unidade


main()