"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que calcula o fatorial de um número inteiro
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    numero = int(input('Digite um número inteiro: '))

    fatorial = 1
    for i in range(2, numero + 1):
        fatorial *= i

    print(fatorial) 


main()