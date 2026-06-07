"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    num = float(input('Digite um número qualquer: '))

    part_frac = obter_part_frac(num)

    if part_frac == 0:
        print('Inteiro')
    else:
        print('Decimal')


def obter_part_frac(n):
    part_int = n // 1
    frac = n - part_int
    return frac


main()