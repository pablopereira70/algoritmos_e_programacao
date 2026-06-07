"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

import turtle
import math

def main():
    num_pieces = int(input('Digite a quantidade de pedaços: '))
    side = 100
    angle = 360 / num_pieces
    bob = turtle.Turtle()
    base = 2 * side * math.sin(math.radians(angle / 2))

    bob.shape('turtle')
    bob.shapesize(1,1,1)
    bob.color('blue')
    bob.pencolor('blue')
    draw_pie(bob, num_pieces, side, angle, base)
    
    bob.hideturtle()
    turtle.mainloop()


def draw_pie(t, n, s, â, b):
    x = 1
    for i in range(n):
        draw_pieces(t, s, â, b)
        t.left(â * x)
        x += 1



def draw_pieces(t, s, â, b):
    t.forward(s)
    t.left(180 - (180 - â) / 2)
    t.forward(b)
    t.home()


main()