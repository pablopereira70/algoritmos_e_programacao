"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para desenhar um polígono regular usando a biblioteca turtle
Autor: Pablo Pereira
Data: Maio / 2026
"""

import turtle

def main():
    bob = turtle.Turtle()
    lenght = int(input('Digite o tamanho do lado: '))
    n = int(input('Digite a quantidade de lados: '))
    polygan(bob, lenght, n)
    turtle.mainloop()


def polygan(t: turtle, lenght, n):
    for i in range(n):
        t.forward(lenght)
        t.left(360/n)


main()