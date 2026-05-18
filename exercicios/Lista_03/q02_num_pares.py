"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que imprime todos os números pares de 1 até N
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    N = int(input('Digite um número qualquer: '))
    
    for i in range(2, N + 1, 2):
        print(i)


main()