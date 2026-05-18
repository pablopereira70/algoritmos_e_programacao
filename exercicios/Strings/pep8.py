"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para converter nomes de variáveis entre os estilos PEP8 e CamelCase.
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *


def main():
    menu = '''
--------  APP PEP8 --------
[1] inserir nome de variável
[2] converter para o inverso
[3] exibir nome de variável
[0] sair
---------------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo('-->', 0, 3)
        if comando == 1:
            var_nome, var_cod = obter_nome_variavel_valido()
        elif comando == 2:
            var_nome, var_cod = converter_codific_inversa(var_nome, var_cod)
        elif comando == 3:
            print(var_nome + ' (' + var_cod + ')')
        else:
            break


def obter_nome_variavel_valido():
    while True:
        try:
            var_nome = obter_texto('Nome da variável: ')
            var_cod = obter_texto('Codificação da variável: ')
            if eh_valida(var_nome, var_cod):
                return var_nome, var_cod
            erro = 1 / 0
        except:
            print('ENTRADA INVÁLIDA')


def eh_valida(var_nome, var_cod):
    if var_cod == 'PEP8':
        for ch in var_nome:
            if eh_maiscula(ch):
                return False
    elif var_cod == 'CAMELCASE':
        for ch in var_nome:
            if ch == '_':
                return False
    else:
        return False
    return True


def eh_maiscula(caractere):
    if ord(caractere) >= 65 and ord(caractere) <= 90:
        return True
    else:
        return False
    

def converter_codific_inversa(var_nome, var_cod):
    if var_cod == 'PEP8':
        return converter_p_camelcase(var_nome), 'CAMELCASE'
    else:
        return converter_p_pep8(var_nome), 'PEP8'
    

def converter_p_camelcase(nome):
    novo_nome = ''
    capslock = False
    for ch in nome:
        if ch == '_':
            capslock = True
            continue
        if capslock:
            novo_nome += chr(ord(ch) - 32)
            capslock = False
        else:
            novo_nome += ch
    return novo_nome


def converter_p_pep8(nome):
    novo_nome = ''
    for ch in nome:
        if eh_maiscula(ch):
            novo_nome += '_' + chr(ord(ch) + 32)
        else:
            novo_nome += ch
    return novo_nome


main()