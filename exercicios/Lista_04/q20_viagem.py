"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main(): 
    menu = '''
--- APP_DESEMPENHO_DO_CARRO ---
[1] para iniciar
[0] para sair
-------------------------------'''
    
    while True:
        exibir(menu)
        comando = obter_inteiro('--> ')
        limpar_tela()
        enter()
        limpar_tela()

        if comando == 1:
            dist_viagem = obter_inteiro_positivo('Digite a distância total da sua viagem(km): ')
            capac_tanque = obter_inteiro_positivo('Digite a capacidade do tanque de combustível(l): ')
            dist_percorrida_total = 0
            paradas = 0
            tanque_consumido_total = 0
            soma_consumo_medio = 0
            registros = 0
            limpar_tela()
            enter()
            limpar_tela()

            while dist_percorrida_total < dist_viagem:
                dist_percorrida_trecho = obter_inteiro_positivo('Digite a distância percorrida no trecho(km): ')
                dist_percorrida_total += dist_percorrida_trecho
                tanque_consumido_trecho = obter_inteiro_positivo('Digite a quantidade de combustível consumida no trecho(l): ')
                tanque_consumido_total += tanque_consumido_trecho
                soma_consumo_medio += dist_percorrida_trecho / tanque_consumido_trecho
                registros += 1

                if tanque_consumido_total > capac_tanque:
                    tanque_consumido_total = 0
                    paradas += 1

                exibir_parcial(paradas, dist_percorrida_trecho, tanque_consumido_trecho)
                enter()
                limpar_tela()

            exibir_total(paradas, registros, soma_consumo_medio)
            enter()
        elif comando == 0:
            break
        else:
            exibir('COMANDO DESCONHECIDO')


def exibir_parcial(p, d, t):
    exibir(f'''
-------------- PARCIAL --------------
Paradas no posto:               {p}
Consumo de combustível(trecho): {d / t:.1f}km/l 
-------------------------------------''')


def exibir_total(p, r, m):
    exibir(f'''
--------------- TOTAL ---------------
Paradas no posto:              {p}
Consumo de combustível(total): {m / r:.1f}km/l
-------------------------------------''')


main()