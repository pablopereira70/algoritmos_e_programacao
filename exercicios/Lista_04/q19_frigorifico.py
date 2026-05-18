"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para ler os dados de um frigorífico e determinar qual é o boi mais gordo e qual é o boi mais magro
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    ident_boi_mais_gordo = ''
    peso_boi_mais_gordo = 0
    ident_boi_mais_magro = ''
    peso_boi_mais_magro = 999

    while True:
        exibir('--- APP_FRIGORÍFICO ---')
        ident = obter_texto('Identificação do cartão: ')

        if ident == '0':
            break

        peso = obter_real_positivo('Peso do cartão(kg): ')
        exibir('------------------------------')
        enter()
        limpar_tela()

        if peso > peso_boi_mais_gordo:
            peso_boi_mais_gordo = peso
            ident_boi_mais_gordo = ident
        elif peso < peso_boi_mais_magro:
            peso_boi_mais_magro = peso
            ident_boi_mais_magro = ident

    exibir(F'''
------- RESULTADOS -------
--> BOI MAIS GORDO
Nº identificação: {ident_boi_mais_gordo}
Peso(kg):         {peso_boi_mais_gordo}
--> BOI MAIS MAGRO
Nº identificação: {ident_boi_mais_magro}
Peso(kg):         {peso_boi_mais_magro}
--------------------------''')


main()