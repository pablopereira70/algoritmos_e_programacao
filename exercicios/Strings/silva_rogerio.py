"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para transformar um nome.
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP SILVA/ROGÉRIO ---
[1] para iniciar
[0] para sair
----------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo("-->", 0, 1)

        if comando == 1:
            nome = obter_texto('Digite o nome: ')
            primeiro_nome = obter_primeiro_nome(nome)
            ultimo_nome = obter_ultimo_nome(nome)
            if primeiro_nome == ultimo_nome:
                print('Desculpe, algo errado aconteceu')
            else:
                print(f"{ultimo_nome}/{primeiro_nome}")
        else:
            break

    print("xauuu")


def obter_primeiro_nome(nome):
    primeiro_nome = ''
    for i in range(len(nome)):
        if nome[i] == ' ':
            return primeiro_nome
        primeiro_nome += nome[i]
    return primeiro_nome

def obter_ultimo_nome(nome):
    ultimo_nome = ''
    for i in range(len(nome)):
        if nome[i] == ' ':
            ultimo_nome = ''
        ultimo_nome += nome[i]
    return ultimo_nome


main()