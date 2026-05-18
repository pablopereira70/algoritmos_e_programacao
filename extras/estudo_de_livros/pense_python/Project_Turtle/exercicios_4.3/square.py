"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para desenhar um quadrado usando a biblioteca turtle
Data: Maio / 2026
"""

import turtle

def main():
    bob = turtle.Turtle()
    lenght = int(input('Digite o lado do quadrado: '))
    square(bob, lenght)
    turtle.mainloop()


def square(t: turtle, lenght):
    for i in range(4):
        t.forward(lenght)
        t.left(90)


main()