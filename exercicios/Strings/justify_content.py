"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para justificar o conteúdo de uma palavra
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP JUSTIFY CONTENT ---
[1] para inserir a palavra
[2] para preencher à esquerda
[3] para preencher à direita
[4] para exibir a palavra
[0] para sair
---------------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo('-->', 0, 4)
        if comando == 1:
            palavra = obter_texto('Digite a palavra: ')
        elif comando == 2:
            try:
                palavra = preencher_esquerda(palavra)
            except:
                print('Desculpe, nenhuma palavra inserida')
        elif comando == 3:
            try:
                palavra = preencher_direita(palavra)
            except:
                print('Desculpe, nenhuma palavra inserida')
        elif comando == 4:
            try:
                print(palavra)
            except:
                print('Desculpe, nenhuma palavra inserida')
        else:
             break
        

def preencher_esquerda(texto):
    espaco = obter_inteiro_positivo('Digite o nº preenchimentos: ')
    preencher = obter_texto_maximo('Digite o caractere: ', 1)
    if preencher == '':
        return espaco * ' ' + texto
    else:
        return espaco * preencher + texto
    

def preencher_direita(texto):
    espaco = obter_inteiro_positivo('Digite o nº preenchimentos: ')
    preencher = obter_texto_maximo('Digite o caractere: ', 1)
    if preencher == '':
        return texto + espaco * ' '
    else:
        return texto + espaco * preencher


main()