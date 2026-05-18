"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que imprime os números ímpares entre dois limites fornecidos pelo usuário.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    for i in range(limite_inferior, limite_superior):
        if i % 2 != 0:
            print(i)


main()