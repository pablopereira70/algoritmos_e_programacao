"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para desenhar um arco usando a biblioteca turtle
Autor: Pablo Pereira
Data: Maio / 2026
"""

import turtle

def main():
    bob = turtle.Turtle()
    raio = int(input('Digite o raio do circulo: '))
    angle = int(input('Digite o ângulo do arco: '))
    arc(bob, raio, angle)
    turtle.mainloop()


def arc(t: turtle, r, angle):
    lenght = 2 * 3.14 * r * angle / 360
    n = int(lenght / 3) + 1
    step_lenght = lenght / n
    step_angle = angle / n
    for i in range(n):
        t.forward(step_lenght)
        t.left(step_angle)


main()