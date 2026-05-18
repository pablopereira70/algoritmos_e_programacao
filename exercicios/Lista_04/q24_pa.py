"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para gerar os termos de uma progressão aritmética (PA)
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP_PROGRESSÃO_ARITMÉTICA ---
[1] para iniciar
[0] para sair
---------------------------------'''

    while True:
        exibir(menu)
        comando = obter_inteiro('--> ')
        limpar_tela()
        enter()
        limpar_tela()

        if comando == 1:
            razao = obter_inteiro('Digite a razão da PA: ')
            inicial = obter_inteiro('Digite o primeiro termo: ')
            num_termos = obter_inteiro('Digite o número de termos: ')
            termos = ''
            termos = str(inicial) + ' - '
            termo = inicial
            limpar_tela()

            while num_termos > 1:
                termo += razao
                termos = termos + str(termo) + ' - '
                num_termos -= 1

            termos += 'FIM'
            exibir(termos)
            enter()
            limpar_tela()
        elif comando == 0:
            break
        else:
            exibir('COMANDO DESCONHECIDO')


main()