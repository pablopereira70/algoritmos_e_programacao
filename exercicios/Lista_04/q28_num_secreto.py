"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para criar um jogo de adivinhação
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *
import random

def main():
    menu = '''
--- APP_NÚMERO_SECRETO ---
[1] para iniciar
[0] para sair
--------------------------'''
    
    while True:
        exibir(menu)
        comando = obter_inteiro_intervalo(0, 1)
        limpar_tela()
        enter()
        limpar_tela()

        if comando == 1:
            num_secreto = random.randint(1, 100)
            tentativas = 0
            exibir('Um número foi sorteado tente acertar!')

            while True:
                num_chute = obter_inteiro_intervalo(1, 100)
                tentativas += 1
                limpar_tela()
                enter()
                limpar_tela()

                if num_chute == num_secreto:
                    break

                dica = obter_dica(num_secreto, num_chute)
                exibir(dica)

            limpar_tela()
            exibir(f'PARABÉNS! você acertou após {tentativas} tentativas')
            enter()
            limpar_tela()
        else:
            break


def obter_dica(ns, nc):
    if ns < nc:
        return 'ERROU! O número secreto é menor'
    else:
        return 'ERROU! O número secreto é maior'


main()