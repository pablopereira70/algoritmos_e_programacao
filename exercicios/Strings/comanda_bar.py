"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP COMANDA DE BAR ---
[1] inserir novo produto
[2] exibir a conta
[3] pagar a conta
[0] sair
--------------------------'''
    valor_total = 0
    while True:
        print(menu)
        comando = obter_inteiro_intervalo('-->', 0, 3)
        if comando == 1:
            valor_total += inserir_produto()
        elif comando == 2:
            try:
                print(f'Valor total: R$ {valor_total:.2f}')
                print(f'Taxa de serviço: R$ {valor_total * 0.1:.2f}')
            except:
                print('Nenhum produto inserido ainda.')
        elif comando == 3:
            pagar_conta(valor_total)
            valor_total = 0
        else:
            break


def inserir_produto():
    while True:
        quant = obter_inteiro_positivo('Quantidade: ')
        cod = obter_texto_maximo('Código do produto: ', 1)
        if eh_produto_valido(cod):
            return quant * obter_preco_produto(cod)
        else:
            print('Esse produto não existe!')


def eh_produto_valido(cod):
    if cod == 'C' or cod == 'A' or cod == 'T' or cod == 'R':
        return True
    else:
        return False
    

def obter_preco_produto(cod):
    if cod == 'C':
        return 9
    elif cod == 'A': 
        return 4
    elif cod == 'T':
        return 32
    else:
        return 8
    

def pagar_conta(conta):
    pago = 0
    taxa = conta * 0.1
    contador = 1

    while pago < conta + taxa:
        pago += obter_real_positivo(f'{contador}º pagamento: ')
        contador += 1

    if pago > conta + taxa:
        print(f'Troco: R$ {pago - conta - taxa:.2f}')


main()