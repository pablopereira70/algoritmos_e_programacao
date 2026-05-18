"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que lê N números e imprime o maior deles.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    n = int(input('Digite a quantidade de números: '))
    
    maior = 0
    for i in range(n):
        num = int(input('Digite um número: '))
        if num > maior:
            maior = num
    
    print(maior)


main()