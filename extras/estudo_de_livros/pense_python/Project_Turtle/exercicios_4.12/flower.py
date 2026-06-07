"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

import turtle

def main():
    num_petals = int(input('Digite a quantidade de pétalas: '))
    radius = 100
    bob = turtle.Turtle()

    bob.shape('turtle')
    bob.shapesize(1,1,1)
    bob.color('blue')
    bob.pencolor('blue')
    draw_flower(bob, num_petals, radius)

    bob.hideturtle()
    turtle.mainloop()


def draw_flower(t, n, r):
    angle = 360 / n
    r = radius_adjusted(r, n)
    angle = especial_case(n, angle)
    for i in range(n):
        draw_petal(t, r, angle)
        t.left(angle)


def draw_petal(t, r, angle):
    length = 2 * 3.14159 * r * (angle/360)
    segment = int(length / 3) + 1
    step_length = length / segment
    step_angle = angle / segment
    for i in range(2):
        for i in range(segment):
            t.forward(step_length)
            t.left(step_angle)
        t.left(180 - angle)


def radius_adjusted(r, n):
    if n > 2:
        adjusted = (n / 2) * (r * 0.2)
        return r + adjusted
    else:
        return r


def especial_case(n, â):
    if n < 3:
        return 90
    else:
        return â


main()