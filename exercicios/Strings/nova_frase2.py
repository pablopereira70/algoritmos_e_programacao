"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP NOVA FRASE2 ---
[1] para iniciar
[0] para sair
----------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo("-->", 0, 1)

        if comando == 1:
            texto = obter_texto('Digite o texto: ')
            novo_texto = my_fun(texto)
            print(novo_texto)
        else:
            break

def my_fun(texto):
    novo_texto = ''

    for ch in texto:
        novo_texto += 2 * ch

    return novo_texto


main()