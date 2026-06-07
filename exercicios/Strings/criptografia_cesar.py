"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP CRIPTOGRAFIA DE CESAR ---
[1] para iniciar
[0] para sair
---------------------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo("-->", 0, 1)
        if comando == 1:
            mensagem = obter_texto("Digite a mensagem: ")
            chave = obter_inteiro_positivo("Digite a chave: ")
            mensagem_criptografada = obter_mensagem_criptografada(mensagem, chave)
            print(mensagem_criptografada)
        else:
            break


def obter_mensagem_criptografada(msg, num):
    msg_cripto = ''
    
    for ch in msg:
        msg_cripto += chr(ord(ch) + num)

    return msg_cripto


main()