"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    n = int(input('Digite o número de termos: '))

    sub = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            s = -(i - sub) / i
        else:
            s = i / (i - sub)
        sub += 1
        print(s)


main()