"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP_SIMULA_EMPRÉSTIMO --
[1] para iniciar
[0] para sair
----------------------------'''
    while True:
        exibir(menu)
        comando = obter_inteiro("--> ")
        limpar_tela()
        enter()
        limpar_tela()

        if comando == 1:
            emprestimo = obter_real_positivo('Digite o valor do empréstimo: ')
            limpar_tela()
            enter()
            limpar_tela()
            juros_diario = obter_real_positivo('Digite em decimal a porcentagem de juros diária: ')
            limpar_tela()
            enter()
            limpar_tela()
            pagamento_diario = obter_real_positivo('Digite o valor diário de pagamento: ')
            limpar_tela()
            enter()
            limpar_tela()
            dias_uteis = obter_dias_uteis(emprestimo, juros_diario, pagamento_diario)
            exibir_simulacao(emprestimo, juros_diario, pagamento_diario, dias_uteis)
            enter()
            limpar_tela()
        elif comando == 0:
            break
        else:
            exibir('COMANDO DESCONHECIDO')


def obter_dias_uteis(emp, jur, pag):
    dias = 0
    debito = emp

    while debito > 0:
        dias += 1
        add = debito * jur
        debito += add
        debito -= pag

    return dias


def exibir_simulacao(emp, jur, pag, dia):
    exibir(f'''
--- SIMULAÇÃO_DE_EMPRÉSTIMO ---
Empréstimo:       {emp:.2f}R$
Juros diários:    {(jur * 100):.2f}%
Pagamento diário: {pag:.2f}R$
Dias úteis:       {dia}d
-------------------------------''')


main()