"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para converter um número decimal em binário e hexadecimal
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP_SISTEMAS_DE_NUMERAÇÃO ---
[1] para inserir um número
[0] para sair
---------------------------------'''

    while True:
        exibir(menu)
        comando = obter_inteiro("--> ")
        limpar_tela()
        enter()
        limpar_tela()

        if comando == 1:
            numero = obter_inteiro_intervalo(0, 255)
            limpar_tela()
            enter()
            limpar_tela()
            exibir_numero(numero)
            enter()
            limpar_tela()
        elif comando == 0:
            break
        else:
            exibir('COMANDO DESCONHECIDO')


def exibir_numero(n):
    decimal = n
    binario = converter_dec_bin(decimal)
    hexadecimal = converter_dec_hex(decimal)

    exibir(f'''
--- CONVERSÃO_DE_BASE --
Decimal:     {decimal}
Binário:     {binario}
Hexadecimal: {hexadecimal}
------------------------''')
    

def converter_dec_bin(dec):
    bin = ''
    resto = dec % 2
    quociente = dec // 2
    bin = str(resto) + bin
    
    while quociente > 0:
        resto = quociente % 2
        quociente //= 2
        bin = str(resto) + bin

    return bin


def converter_dec_hex(dec):
    hex = ''
    resto = verificar_se_letra_hex(dec % 16)
    quociente = dec // 16
    hex = str(resto) + hex
    
    while quociente > 0:
        resto = verificar_se_letra_hex(quociente % 16)
        quociente //= 16
        hex = str(resto) + hex

    return hex


def verificar_se_letra_hex(n):
    if n == 15:
        return 'F'
    elif n == 14:
        return 'E'
    elif n == 13:
        return 'D'
    elif n == 12:
        return 'C'
    elif n == 11:
        return 'B'
    elif n == 10:
        return 'A'
    else:
        return n


main()