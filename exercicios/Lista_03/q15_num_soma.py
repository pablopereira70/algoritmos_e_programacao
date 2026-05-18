"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que imprime a soma dos números de 1 até N a cada iteração.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    n = int(input('Digite o número de termos: '))

    num = 0
    for i in range(1, n + 1):
        num += i
        print(num)


main() 