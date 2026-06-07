"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    n = int(input('Digite o número de termos: '))

    den = 1
    for i in range(1, n + 1):
        s = den / i
        den += 2
        print(s)


main()