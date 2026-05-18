"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para criptografar uma frase
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP CRIPTOGRAFIA DA ALEGRIA ---
[1] para iniciar
[0] para sair
-----------------------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo("-->", 0, 1)
        if comando == 1:
            texto = obter_texto("Digite a frase: ")
            texto_criptografado = obter_texto_criptografado(texto)
            print(texto_criptografado)
        else:
            break


def obter_texto_criptografado(texto):
    texto_cripto = ''

    for ch in texto:
        if eh_vogal(ch):
            texto_cripto = str(ord(ch)) + texto_cripto
        elif eh_cosoante(ch):
            texto_cripto = chr(ord(ch) - 1) + texto_cripto
        else:
            texto_cripto = ch + texto_cripto

    return texto_cripto


def eh_vogal(caractere):
    if ord(caractere) == 65 or ord(caractere) == 69 or ord(caractere) == 73 or ord(caractere) == 79 or ord(caractere) == 85 or ord(caractere) == 97 or ord(caractere) == 101 or ord(caractere) == 105 or ord(caractere) == 111 or ord(caractere) == 117:
        return True
    else:
        return False


def eh_cosoante(caractere):
    if ord(caractere) >= 66 and ord(caractere) <= 90 or ord(caractere) >= 98 and ord(caractere) <= 122:
        return True
    else:
        return False


main()