"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    n = int(input('Digite um número inteiro: '))
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    for i in range(limite_inferior, limite_superior):
        if i % n == 0:
            print(i)


main()