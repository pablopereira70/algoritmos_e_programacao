"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

import turtle

def main():
    bob = turtle.Turtle()
    raio = int(input('Digite o raio do circulo: '))
    circle(bob, raio)
    turtle.mainloop()


def polygan(t: turtle, lenght, n):
    for i in range(n):
        t.forward(lenght)
        t.left(360/n)


def circle(t, r):
    circumference = 2 * 3.14 * r
    n = int(circumference / 3) + 1
    lenght = circumference  / n
    polygan(t, lenght, n)


main()