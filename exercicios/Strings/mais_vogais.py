"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para analisar uma frase
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP MAIS VOGAIS ---
[1] para iniciar
[0] para sair
-----------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo('-->', 0, 1)
        if comando == 1:
            texto = obter_texto('Digite o texto: ')
            quant_vogal = contar_vogais(texto)
            print(f'Palavra: {texto}')
            print(f'Vogais:  {quant_vogal / len(texto) * 100:.0f}%')
        else:
            break


def contar_vogais(texto):
    count = 0
    for ch in texto:
        if eh_vogal(ch):
            count += 1
        elif eh_vogal_acentuada(ch):
            count += 1
    return count


def eh_vogal(caractere):
    if ord(caractere) == 65 or ord(caractere) == 69 or ord(caractere) == 73 or ord(caractere) == 79 or ord(caractere) == 85 or ord(caractere) == 97 or ord(caractere) == 101 or ord(caractere) == 105 or ord(caractere) == 111 or ord(caractere) == 117:
        return True
    else:
        return False
    

def eh_vogal_acentuada(caractere):
    if ord(caractere) >= 249 and ord(caractere) <= 251 or ord(caractere) >= 242 and ord(caractere) <= 245 or ord(caractere) >= 236 and ord(caractere) <= 238 or ord(caractere) >= 224 and ord(caractere) <= 227 or ord(caractere) >= 232 and ord(caractere) <= 234 or ord(caractere) >= 217 and ord(caractere) <= 219 or ord(caractere) >= 210 and ord(caractere) <= 213 or ord(caractere) >= 200 and ord(caractere) <= 202 or ord(caractere) >= 204 and ord(caractere) <= 206 or ord(caractere) >= 192 and ord(caractere) <= 195:
        return True
    else:
        return False


main()