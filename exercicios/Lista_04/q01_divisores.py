"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    while True:
        print("FLAG NÚMERO = 0 ")
        numero = obter_inteiro("Digite um número inteiro: ")

        if numero == 0:
            break

        divisores = obter_divisores(numero)
    
        print(f"Número:    {numero}")
        print(f"Divisores: {divisores}") 


def obter_divisores(n):
    divs = ""

    if n > 0:

        for i in range(n, 0, -1):

            if n % i == 0:
                divs += str(i) + " "

    else:

        for i in range(n, 0, 1):

            if n % i == 0:
                divs += str(i) + " "

    return divs
        
        
main()