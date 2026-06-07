"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP_MULTIPLICAÇÃO ---
[1] para iniciar
[0] para sair
-------------------------'''

    while True:
        exibir(menu)
        comando = obter_inteiro('--> ')
        limpar_tela()
        enter()
        limpar_tela()

        if comando == 1:
            multiplicando = obter_inteiro('Digite o multiplicando: ')
            multiplicador = obter_inteiro('Digite o multiplicador: ')
            produto = obter_produto(multiplicando, multiplicador)
            sinal = obter_sinal(multiplicando, multiplicador)
            limpar_tela()
            exibir(f'{multiplicando} * {multiplicador} = {sinal}{produto}')
            enter()
            limpar_tela()
        elif comando == 0:
            break
        else:
            exibir('COMANDO DESCONHECIDO')


def obter_produto(num1, num2):
    num_vezes = transformar_positivo(num1)
    incremento = transformar_positivo(num2)
    produto = 0

    for i in range(num_vezes):
        produto += incremento

    return produto


def obter_sinal(num1, num2):
    if num1 >= 0 and num2 >= 0 or num1 <= 0 and num2 <= 0:
        return ''
    else:
        return '-'


main()