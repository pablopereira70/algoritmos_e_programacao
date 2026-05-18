"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que imprime os N primeiros termos da sequência de Fibonacci.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    n = int(input('Digite o número de termos: '))

    elem_1 = 1
    elem_2 = 0
    print(elem_2)
    print(elem_1)
    for i in range(n - 2):
        fib = elem_1 + elem_2
        elem_2 = elem_1
        elem_1 = fib
        print(fib)


main()