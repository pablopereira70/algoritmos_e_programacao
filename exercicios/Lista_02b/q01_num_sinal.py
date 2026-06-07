"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    numero = int(input('Digite um número inteiro qualquer: '))
    if numero > 0:
        print(f'O número {numero} é positivo')
    elif numero < 0:
        print(f'O número {numero} é negativo')
    else:
        print(f'O número {numero} é nulo')


main()