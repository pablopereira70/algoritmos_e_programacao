"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que recebe um número inteiro qualquer e verifica se ele é par, ímpar ou nulo. 
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    num = int(input('Digite um número inteiro qualquer: '))
    
    if num != 0:
        eh_par = num % 2 == 0
        if eh_par:
            print(f'O número {num} é par')
        else:
            print(f'O número {num} é ímpar')
    else:
        print(f'O número {num} é nulo')


main()