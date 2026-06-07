"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    n = int(input('Digite um número inteiro: '))

    soma = 0
    for i in range(1, n + 1):
        soma += i
        
    print(soma)


main()