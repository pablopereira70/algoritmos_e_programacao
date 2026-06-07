"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    n = int(input('Digite a quantidade de termos: '))

    for i in range(1, n + 1):
        s = 1 / i
        if i % 2 == 0:
            print(-s)
        else:
            print(s)


main()