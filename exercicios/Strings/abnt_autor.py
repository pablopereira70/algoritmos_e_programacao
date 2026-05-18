"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para formatar nomes de autores conforme as normas da ABNT
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP ABNT AUTOR ---
[1] para iniciar
[0] para sair
----------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo('-->', 0, 1)
        if comando == 1:
            nome =  obter_texto('Digite o nome: ')
            ultimo_nome = obter_ultimo_nome(nome)
            iniciais = obter_iniciais(nome)
            print(my_title(ultimo_nome) + ', ' + my_upper(iniciais))
        else:
            break


def obter_ultimo_nome(texto):
    ultimo_nome = ''
    for ch in texto:
        if ch == ' ':
            ultimo_nome = ''
            continue
        ultimo_nome += ch
    return ultimo_nome


def obter_iniciais(texto):
    iniciais = texto[0] + '.'
    for i in range(len(texto)):
        if texto[i] == ' ':
             iniciais += texto[i + 1] + '.'
    return iniciais[:len(iniciais) - 2]


def my_upper(texto):
    texto_upper = ''
    for ch in texto:
        if ord(ch) >= 97 and ord(ch) <= 122:
            texto_upper += chr(ord(ch) - 32)
            continue
        texto_upper += ch
    return texto_upper


def my_title(texto):
    novo_texto = ''
    count = 0
    for ch in texto:
        if count == 0:
            if ord(ch) >= 97 and ord(ch) <= 122:
                novo_texto += chr(ord(ch) - 32)
            else:
                novo_texto += ch
            count = 1
        elif count > 0:
            if ord(ch) >= 65 and ord(ch) <= 90:
                novo_texto += chr(ord(ch) + 32)
            else:
                novo_texto += ch
    return novo_texto

         


main()