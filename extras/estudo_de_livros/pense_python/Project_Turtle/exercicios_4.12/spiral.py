"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para desenhar uma espiral usando a biblioteca turtle
Autor: Pablo Pereira
Data: Maio / 2026
"""

import turtle

def main():
    bob = turtle.Turtle()
    radius = 25
    angle = 90

    bob.shape('turtle')
    bob.shapesize(1,1,1)
    bob.color('blue')
    bob.pencolor('blue')
    draw_spiral(bob, radius, angle)

    bob.hideturtle()
    turtle.mainloop()


def draw_spiral(t, r, â):
    for i in range(20):
        arc(t, r, â)
        r *= 1.1


def arc(t, r, â):
    lenght = 2 * 3.14 * r * â / 360
    n = int(lenght / 3) + 1
    step_lenght = lenght / n
    step_angle = â / n
    for i in range(n):
        t.forward(step_lenght)
        t.left(step_angle)


main()