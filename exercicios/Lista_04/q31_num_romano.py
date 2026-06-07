"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP_NÚMERO_ROMANO ---
[1] para iniciar
[0] para sair
-------------------------'''
        
    while True:
        exibir(menu)
        comando = obter_inteiro_intervalo(0, 1)
        limpar_tela()
        enter()
        limpar_tela()

        if comando == 1:
            num_decimal = obter_inteiro_intervalo(1, 9999)
            limpar_tela()
            quant_m, resto = obter_quant_m(num_decimal)
            quant_d, resto = obter_quant_d(resto)
            quant_c, resto = obter_quant_c(resto)
            quant_l, resto = obter_quant_l(resto)
            quant_x, resto = obter_quant_x(resto)
            quant_v, resto = obter_quant_v(resto)
            quant_i = obter_quant_i(resto)
            num_romano = quant_m + quant_d + quant_c + quant_l + quant_x + quant_v + quant_i
            exibir(f'''
--- CONVERSÃO ---
Decimal: {num_decimal} 
Romano:  {num_romano}
-----------------''')
            enter()
            limpar_tela()
        else:
            break


def obter_quant_m(n):
    quociente = n // 1000
    resto = n % 1000
    return 'M' * quociente, resto


def obter_quant_d(n):
    if n >= 900:
        return 'CM', n - 900
    else:
        quociente = n // 500
        resto = n % 500
        return 'D' * quociente, resto


def obter_quant_c(n):
    if n >= 400:
        return 'CD', n - 400
    else:
        quociente = n // 100
        resto = n % 100
        return 'C' * quociente, resto


def obter_quant_l(n):
    if n >= 90:
        return 'XC', n - 90
    else:
        quociente = n // 50
        resto = n % 50
        return 'L' * quociente, resto


def obter_quant_x(n):
    if n >= 40:
        return 'XL', n - 40
    quociente = n // 10
    resto = n % 10
    return 'X' * quociente, resto


def obter_quant_v(n):
    if n >= 9:
        return 'IX', n - 9
    else:
        quociente = n // 5
        resto = n % 5
        return 'V' * quociente, resto


def obter_quant_i(n):
    if n == 4:
        return 'IV'
    else:
        return 'I' * n


main()