"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para realizar uma pesquisa de audiência
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP_PESQUISA_AUDIÊNCIA ---
[1] para iniciar
[0] para sair
------------------------------'''
    
    while True:
        exibir(menu)
        comando = obter_inteiro('--> ')
        limpar_tela()
        enter()
        limpar_tela()

        if comando == 1:
            entrevistados = 0
            canal_2 = 0
            canal_4 = 0
            canal_5 = 0
            canal_7 = 0
            canal_10 = 0
            
            while True:
                exibir_canais()
                canal = obter_inteiro('--> ')
                limpar_tela()
                enter()
                limpar_tela()
                
                if canal == 0:
                    break
                elif canal == 2:
                    canal_2 += 1
                    entrevistados += 1
                elif canal == 4:
                    canal_4 += 1
                    entrevistados += 1
                elif canal == 5:
                    canal_5 += 1
                    entrevistados += 1
                elif canal == 7:
                    canal_7 += 1
                    entrevistados += 1
                elif canal == 10:
                    canal_10 += 1
                    entrevistados += 1
                else:
                    exibir('CANAL INEXISTENTE')
                    enter()
                    limpar_tela()
        elif comando == 0:
            break
        else:
            exibir('COMANDO DESCONHECIDO')

        exibir(f'''
--- AUDIÊNCIA ---
Canal 2:  {canal_2 / entrevistados * 100:.1f}%
Canal 4:  {canal_4 / entrevistados * 100:.1f}%
Canal 5:  {canal_5 / entrevistados * 100:.1f}%
Canal 7:  {canal_7 / entrevistados * 100:.1f}%
Canal 10: {canal_10 / entrevistados * 100:.1f}%
-----------------''')
        enter()
        

def exibir_canais():
    exibir(f'''
--- OPÇÕES ---
[2]  Canal 2
[4]  Canal 4
[5]  Canal 5
[7]  Canal 7
[10] Canal 10
[0] FIM
--------------''')


main()