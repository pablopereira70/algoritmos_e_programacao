"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que imprime os múltiplos de um número N dentro de um intervalo definido
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    n = int(input('Digite um número inteiro: '))
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    for i in range(limite_inferior, limite_superior):
        if i % n == 0:
            print(i)


main()