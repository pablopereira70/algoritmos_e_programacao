"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para ler os dados de um concurso de beleza e determinar quem é a mais alta, a mais baixa, a mais gorda e a mais magra
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    nome_mais_alta = ''
    altura_mais_alta = 0.0
    nome_mais_baixa = ''
    altura_mais_baixa = 99.0
    nome_mais_magra = ''
    peso_mais_magra = 999.0
    nome_mais_gorda = ''
    peso_mais_gorda = 0.0

    while True:
        exibir('--- APP_CONCURSO_DE_BELEZA ---')
        nome = obter_texto('Nome do cartão: ')

        if nome == 'FIM':
            break

        altura = obter_real_positivo('Altura do cartão(m): ')
        peso = obter_real_positivo('Peso do cartão(kg): ')
        exibir('------------------------------')
        enter()
        limpar_tela()

        if altura > altura_mais_alta:
            altura_mais_alta = altura
            nome_mais_alta = nome
        elif altura < altura_mais_baixa:
            altura_mais_baixa = altura
            nome_mais_baixa = nome

        if peso > peso_mais_gorda:
            peso_mais_gorda = peso
            nome_mais_gorda = nome
        elif peso < peso_mais_magra:
            peso_mais_magra = peso
            nome_mais_magra = nome

    exibir(f'''
----- RESULTADOS -----
           
--> MAIS GORDA 
Nome: {nome_mais_gorda}
Peso: {peso_mais_gorda:.1f}kg

--> MAIS MAGRA
Nome: {nome_mais_magra}
Peso: {peso_mais_magra:.1f}kg

--> MAIS ALTA
Nome:   {nome_mais_alta}
Altura: {altura_mais_alta:.2f}m

--> MAIS BAIXA
Nome:   {nome_mais_baixa}
Altura: {altura_mais_baixa:.2f}m''')


main()