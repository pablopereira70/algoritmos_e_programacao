"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    num = obter_inteiro("Digite um número inteiro: ")

    n = transformar_positivo(num)
    quant_digitos = contar_quant_digitos(n)

    print(f"O número {num} tem {quant_digitos} dígito(s)")


def contar_quant_digitos(n):
    numero = n
    quant = 0

    while True: 
        numero //= 10

        if numero == 0:
            return quant + 1

        quant += 1


main()