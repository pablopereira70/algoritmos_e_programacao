"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    dia = int(input('Digite o dia: '))
    mes = int(input('Digite o mês: '))
    ano = int(input('Digite o ano: '))

    data_valida = verificar_se_data_valida(dia, mes, ano)
    
    if data_valida:
        print(f'a data {dia:2.0f}/{mes:2.0f}/{ano:2.0f} é válida')
    else:
        print(f'a data {dia:2.0f}/{mes:2.0f}/{ano:2.0f} não é válida')


def verificar_se_data_valida(d, m, a):
    return d <= 31 and d > 0 and m <= 12 and m > 0 and a > 0


main()