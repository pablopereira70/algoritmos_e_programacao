"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu =  '''
--- APP_PLACAR ---
[1] para iniciar
[0] para sair
------------------'''

    partidas, vitorias_j1, vitorias_j2, maior_vencedor = ler_info(menu)

    exibir("------- INFORMAÇÕES -------")
    exibir(f"Partidas jogadas:   {partidas}")
    exibir(f"Vitórias jogador 1: {vitorias_j1}")
    exibir(f"Vitórias jogador 2: {vitorias_j2}")
    exibir(f"Maior vencedor:     {maior_vencedor}")


def ler_info(menu):
    partidas = 0
    vitorias_j1 = 0
    vitorias_j2 = 0

    while True:
        exibir(menu)
        comando = obter_inteiro('--> ')
        limpar_tela()
        enter()
        limpar_tela()

        if comando == 1:
            vencedor = iniciar_partida()
            partidas += 1
            if vencedor == 'J1':
                vitorias_j1 += 1
            else:
                vitorias_j2 += 1
        elif comando == 0:
            break

    maior_vencedor = obter_maior_vencedor(vitorias_j1, vitorias_j2)
    
    return partidas, vitorias_j1, vitorias_j2, maior_vencedor


def iniciar_partida():
    pontos_j1 = 0
    pontos_j2 = 0
    vencedor = ''

    while True:
        exibir_placar(pontos_j1, pontos_j2)
        pontos_j1, pontos_j2 = atualizar_placar(pontos_j1, pontos_j2)
        limpar_tela()
        enter()
        limpar_tela()

        if pontos_j1 >= 21 and pontos_j1 - pontos_j2 >= 2:
            vencedor = 'J1'
            break
        elif pontos_j2 >= 21 and pontos_j2 - pontos_j1 >= 2:
            vencedor = 'J2'
            break

    return vencedor
            


def exibir_placar(p1, p2):
    exibir(f'''
---- PLACAR ----
jogador 1: {p1}
jogador 2: {p2}
----------------''')


def atualizar_placar(p1, p2):
    quem_ponto = obter_inteiro("Digite o quem pontuou(1 ou 2): ")

    if quem_ponto == 1:
        return p1 + 1, p2
    elif quem_ponto == 2:
        return p1, p2 + 1
    else:
        return p1, p2
    

def obter_maior_vencedor(v1, v2):
    if v1 > v2:
        return 'Jogador 1'
    elif v1 < v2:
        return 'Jogador 2'
    else:
        return 'Empate'


main()