"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP_DIVISÃO_INTEIRA ---
[1] para iniciar
[0] para sair
---------------------------'''

    while True:
        exibir(menu)
        comando = obter_inteiro('--> ')
        limpar_tela()
        enter()
        limpar_tela()

        if comando == 1:
            dividendo = obter_inteiro('Digite o dividendo: ')
            divisor = obter_inteiro('Digite o divisor: ')
            quociente, resto = obter_quociente_e_resto(dividendo, divisor)
            sinal = obter_sinal(dividendo, divisor)
            limpar_tela()
            exibir(f'{dividendo} // {divisor} = {sinal}{quociente}')
            exibir(f'{dividendo} % {divisor} = {resto}')
            enter()
            limpar_tela()
        elif comando == 0:
            break
        else:
            exibir('COMANDO DESCONHECIDO')


def obter_quociente_e_resto(n1, n2):
    resto = transformar_positivo(n1)
    decremento = transformar_positivo(n2)
    quociente = 0

    while True:
        resto  -= decremento

        if resto < 0:
            resto += decremento
            break

        quociente += 1

    return quociente, resto


def obter_sinal(num1, num2):
    if num1 >= 0 and num2 >= 0 or num1 <= 0 and num2 <= 0:
        return ''
    else:
        return '-'


main()