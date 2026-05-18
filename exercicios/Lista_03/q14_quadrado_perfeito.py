"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que calcula o maior quadrado perfeito menor ou igual a um número inteiro N.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    n = int(input('Digite um número inteiro: '))

    quadrado = 0
    for i in range(1, n):
        temp = i ** 2
        if temp > n:
            break
        quadrado = temp
    
    print(quadrado)


main()