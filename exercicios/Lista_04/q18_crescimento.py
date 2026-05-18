"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para simular o crescimento populacional de duas cidades
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP_CRESCIMENTO_POPULACIONAL ---
[1] para iniciar
[0] para sair
------------------------------------'''

    while True:
        exibir(menu)
        comando = obter_inteiro('--> ')
        limpar_tela()
        enter()
        limpar_tela()

        if comando == 1:
            popul_cidade_a = obter_inteiro_positivo('Digite a quantidade de habitantes da cidade A: ')
            cresc_anual_cidade_a = obter_real_positivo('Digite a taxa anual de crescimento da cidade A em decimal: ')
            popul_cidade_b = obter_inteiro_positivo('Digite a quantidade de habitantes da cidade B: ')
            cresc_anual_cidade_b = obter_real_positivo('Digite a taxa anual de crescimento da cidade B em decimal: ')
            anos_cidade_a_maior_cidade_b = obter_anos_cidade_a_maior_cidade_b(popul_cidade_a, cresc_anual_cidade_a, popul_cidade_b, cresc_anual_cidade_b)
            limpar_tela()
            exibir_resultados(popul_cidade_a, cresc_anual_cidade_a, popul_cidade_b, cresc_anual_cidade_b, anos_cidade_a_maior_cidade_b)
            enter()
            limpar_tela()
        elif comando == 0:
            break
        else:
            exibir('COMANDO DESCONHECIDO')


def obter_anos_cidade_a_maior_cidade_b(pa, ca, pb, cb):
    anos = 0
    populacao_a = pa
    populacao_b = pb

    while populacao_a < populacao_b:
        populacao_a += populacao_a * ca
        populacao_b += populacao_a * cb
        anos += 1

    return anos


def exibir_resultados(pa, ca, pb, cb, a):
    exibir(f'''
------------------- RESULTADOS -------------------
População cidade A:                    {pa}
Taxa anual de crescimento cidade A:    {ca * 100:.2f}%
População cidade B:                    {pb}
Taxa anual de crescimento cidade B:    {cb * 100:.2f}%
Anos necessários para A ultrapassar B: {a}
--------------------------------------------------''')


main()