"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP_SIMULA_INVESTIMENTO ---
[1] para iniciar
[0] para sair
-------------------------------'''

    while True:
        exibir(menu)
        comando = obter_inteiro_intervalo(0, 1)
        limpar_tela()
        enter()
        limpar_tela()

        if comando == 1:
            aporte = obter_real_positivo('Digite o valor do aporte mensal: ')
            juros = obter_real_positivo('Digite em decimal o juros mensal: ')
            limpar_tela()
            enter()
            limpar_tela()
            saldo_investido = 0
            contador = 0

            while contador < 12:
                saldo_investido += aporte
                saldo_investido += saldo_investido * juros
                contador += 1

                if contador == 12:
                    exibir(f'''
--- SIMULAÇÃO_DE_INVESTIMENTO ---
Aporte mensal:   {aporte:.2f}R$
Juros mensal:    {juros *  100:.2f}%
Saldo investido: {saldo_investido:.2f}R$
---------------------------------''')
                    enter()
                    limpar_tela()
                    exibir('''
--- PROCESSAR_MAIS_UM_ANO ---
[1] para sim
[2] para não
-----------------------------''')
                    mais_um_ano = obter_inteiro_intervalo(1, 2)
                    limpar_tela()

                    if mais_um_ano == 1:
                        contador = 0
                        
        else:
            break


main()