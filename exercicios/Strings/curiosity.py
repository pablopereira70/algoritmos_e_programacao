"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP CURIOSITY ---
[1] para iniciar
[0] para sair
---------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo('-->', 0, 1)
        if comando == 1:
            entrada = obter_texto("Mensagem: ")
            erros = obter_erros(entrada)
            print(f'Erros: {erros}')
        else:
            break


def obter_erros(texto):
    erros = 0
    indice = 0
    contador = 1 

    while indice < len(texto):
        if contador == 1:
            esperado = 'H'
        elif contador == 2:
            esperado = 'E'
        elif contador == 3:
            esperado = 'L'
        else:
            esperado = 'P'

        if texto[indice] != esperado:
            erros += 1

        indice += 1
        contador += 1

        if contador > 4:
            contador = 1

    return erros


main()