"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    soma_salarios, soma_salarios_reajustados, diferenca_salarios = ler_salarios()

    exibir('--------------- INFORMAÇÕES ---------------')
    exibir(f'Soma dos salários:             {soma_salarios:.2f}')
    exibir(f'Soma dos salários reajustados: {soma_salarios_reajustados:.2f}')
    exibir(f'Diferença entre as somas:      {diferenca_salarios:.2f}')


def ler_salarios():
    soma_salarios = 0
    soma_salarios_reajustados = 0

    while True:
        salario = obter_real_positivo("Digite o seu salário: ")

        if salario == 0:
            break

        soma_salarios += salario
        salario_reajustado = obter_salario_reajustado(salario)
        soma_salarios_reajustados += salario_reajustado
        limpar_tela()
        exibir(f"Salário reajustado: {salario_reajustado:.2f}")
        enter()
        limpar_tela()

    diferenca_salarios = soma_salarios_reajustados - soma_salarios
    return soma_salarios, soma_salarios_reajustados, diferenca_salarios


def obter_salario_reajustado(sal):
    acrescimo = determinar_acrescimo(sal)
    return sal + acrescimo


def determinar_acrescimo(sal):
    if sal < 2999.99:
        return sal * 0.25
    elif sal < 5999.99:
        return sal * 0.2
    elif sal < 9999.99:
        return sal * 0.15
    else:
        return sal * 0.1


main()