"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para calcular o valor total a pagar por um produto
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP_COMPRAS ---
[1] para iniciar
[0] para sair
-------------------'''

    while True:
        exibir(menu)
        comando = obter_inteiro_intervalo(0, 1)
        limpar_tela()
        enter()
        limpar_tela()

        if comando == 1:
            nome = obter_texto('Digite o nome do produto: ')
            preco = obter_real_positivo('Digite o preço unitário do produto: ')
            quantidade = obter_inteiro_positivo('Digite a quantidade de produto comprada: ')
            limpar_tela()
            valor_total = preco * quantidade
            desconto = obter_desconto(quantidade)
            valor_desconto = valor_total * desconto
            valor_pagar = valor_total - valor_desconto
            exibir(f'''
--------- NOTA_FISCAL ---------
Nome do produto:     {nome}
Preço unitário:      {preco:.2f}R$
Quantidade comprada: {quantidade}
Valor total:         {valor_total:.2f}R$
Desconto:            {desconto * 100:.0f}%
Valor a pagar:       {valor_pagar:.2f}R$
-------------------------------''')
            enter()
            limpar_tela()
        else:
            break


def obter_desconto(quant):
    if quant > 50:
        return 0.25
    elif quant > 20:
        return 0.2
    elif quant > 10:
        return 0.1
    else:
        return 0


main()