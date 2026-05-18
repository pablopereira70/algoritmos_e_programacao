"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para verificar se uma palavra é palíndroma
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP PALÍNDROMA ---
[1] para iniciar
[0] para sair
----------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo('-->', 0, 1)
        if comando == 1:
            texto = obter_texto('Digite a palavra: ')
            eh_palindroma = verificar_eh_palindroma(texto)
            print(f'Palavra:    {texto}')
            print(f'Palíndroma: {eh_palindroma}')
        else:
            break


def verificar_eh_palindroma(texto):
    texto_inverso = ''

    for ch in texto:
        texto_inverso = ch + texto_inverso

    if texto == texto_inverso:
        return 'sim'
    
    return 'não'


main()