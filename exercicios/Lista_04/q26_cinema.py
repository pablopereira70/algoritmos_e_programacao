"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para coletar opiniões de espectadores sobre um filme
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP_CINEMA ---
[1] para iniciar
[0] para sair
------------------'''

    while True:
        exibir(menu)
        comando = obter_inteiro_intervalo(0, 1)
        limpar_tela()
        enter()
        limpar_tela()

        if comando == 1:
            entrevistados = 0
            otimo = 0
            bom = 0
            regular = 0
            pessimo = 0
            idades_otimo = 0

            while True:
                idade = obter_inteiro_positivo('Digite a sua idade: ')
                limpar_tela()

                if idade == 0:
                    break

                exibir_opcoes()
                opiniao = obter_inteiro_intervalo(1, 4)
                limpar_tela()

                if opiniao == 1:
                    otimo += 1
                    idades_otimo += idade
                    entrevistados += 1
                elif opiniao == 2:
                    bom += 1
                    entrevistados += 1
                elif opiniao == 3:
                    regular += 1
                    entrevistados += 1
                else:
                    pessimo += 1
                    entrevistados += 1
        else:
            break

        exibir(f'''
--------------- INFORMAÇÕES ---------------
média das idades que respoderam ótimo: {idades_otimo / otimo:.1f}
quantidade que respondeu regular:      {regular}
percentual que respondeu bom:          {bom / entrevistados * 100:.1f}%
-------------------------------------------
''')
        enter()
        limpar_tela()


def exibir_opcoes():
    exibir('''
--- OPÇÕES ---
[1] ótimo
[2] bom
[3] regular
[4] péssimo
--------------''')


main()