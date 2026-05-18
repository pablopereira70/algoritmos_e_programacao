"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para desenhar letras usando a biblioteca turtle
Autor: Pablo Pereira
Data: Maio / 2026
"""

import turtle

def main():
    letter = input('Digite a letra: ')
    bob = turtle.Turtle()

    bob.shape('turtle')
    bob.shapesize(1,1,1)
    bob.color('blue')
    bob.pencolor('blue')
    search_letter(bob, letter)

    bob.hideturtle()
    turtle.mainloop()


def search_letter(t, l):
    if l == 'a' or l == 'A':
        draw_letter_a(t)
    elif l == 'b' or l == 'B':
        draw_letter_b(t)
    elif l == 'c' or l == 'C':
        draw_letter_c(t)
    elif l == 'd' or l == 'D':
        draw_letter_d(t)
    elif l == 'e' or l == 'E':
        draw_letter_e(t)
    elif l == 'f' or l == 'F':
        draw_letter_f(t)
    elif l == 'g' or l == 'G':
        draw_letter_g(t)
    elif l == 'h' or l == 'H':
        draw_letter_h(t)
    elif l == 'i' or l == 'I':
        draw_letter_i(t)
    elif l == 'j' or l == 'J':
        draw_letter_j(t)
    elif l == 'k' or l == 'K':
        draw_letter_k(t)
    elif l == 'l'or l == 'L':
        draw_letter_l(t)
    elif l == 'm' or l == 'M':
        draw_letter_m(t)
    elif l == 'n' or l == 'N':
        draw_letter_n(t)
    elif l == 'o' or l == 'O':
        draw_letter_o(t)
    elif l == 'p' or l == 'P':
        draw_letter_p(t)
    elif l == 'q' or l == 'Q':
        draw_letter_q(t)
    elif l == 'r' or l == 'R':
        draw_letter_r(t)
    elif l == 's' or l == 'S':
        draw_letter_s(t)
    elif l == 't' or l == 'T':
        draw_letter_t(t)
    elif l == 'u' or l == 'U':
        draw_letter_u(t)
    elif l == 'v' or l == 'V':
        draw_letter_v(t)
    elif l == 'w' or l == 'W':
        draw_letter_w(t)
    elif l == 'x' or l == 'X':
        draw_letter_x(t)
    elif l == 'y' or l == 'Y':
        draw_letter_y(t)
    elif l == 'z' or l == 'Z':
        draw_letter_z(t)
    else:
        print('Letra inválida. Por favor, digite uma letra de A a Z.')


def draw_letter_a(t):
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.backward(40)
    t.right(120)
    t.forward(60)


def draw_letter_b(t):
    t.left(90)
    t.forward(100)  
    t.right(120)
    t.forward(50)
    t.right(120)
    t.forward(50)
    t.left(120)
    t.forward(50)
    t.right(120)
    t.forward(50)


def draw_letter_c(t):
    t.forward(100)
    t.backward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    

def draw_letter_d(t):
    t.left(90)
    t.forward(100)
    t.right(120)
    t.forward(50)
    t.right(60)
    t.forward(50)
    t.right(60)
    t.forward(50)


def draw_letter_e(t):
    t.forward(50)
    t.backward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.backward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)


def draw_letter_f(t):
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.backward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)


def draw_letter_g(t):
    t.backward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)


def draw_letter_h(t):
    t.left(90)
    t.forward(50)
    t.backward(100)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.backward(100)


def draw_letter_i(t):
    t.forward(50)
    t.backward(25)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(25)
    t.backward(50)


def draw_letter_j(t):
    t.forward(80)
    t.backward(40)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(25)


def draw_letter_k(t):
    t.left(90)
    t.forward(100)
    t.backward(50)
    t.right(45)
    t.forward(60)
    t.backward(60)
    t.right(90)
    t.forward(60)


def draw_letter_l(t):
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(50)


def draw_letter_m(t):
    t.left(90)
    t.forward(100)
    t.right(150)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.right(150)
    t.forward(100)


def draw_letter_n(t):
    t.left(90)
    t.forward(100)
    t.right(150)
    t.forward(115)
    t.left(150)
    t.forward(100)


def draw_letter_o(t):
    t.circle(50)


def draw_letter_p(t):
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)


def draw_letter_q(t):
    t.backward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(45)
    t.forward(20)
    t.backward(50)


def draw_letter_r(t):
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(45)
    t.backward(70)


def draw_letter_s(t):
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)


def draw_letter_t(t):
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.backward(100)


def draw_letter_u(t):
    t.right(90)
    t.forward(90)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(90)


def draw_letter_v(t):
    t.right(60)
    t.forward(100)
    t.left(120)
    t.forward(100)


def draw_letter_w(t):
    t.right(90)
    t.forward(100)
    t.left(150)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.left(150)
    t.forward(100)


def draw_letter_x(t):
    t.left(45)
    t.forward(50)
    t.backward(100)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.backward(100)


def draw_letter_y(t):
    t.left(90)
    t.forward(50)
    t.right(45)
    t.forward(60)
    t.backward(60)
    t.left(90)
    t.forward(60)


def draw_letter_z(t):
    t.backward(80)
    t.left(45)
    t.forward(110)
    t.right(45)
    t.backward(80)


main()