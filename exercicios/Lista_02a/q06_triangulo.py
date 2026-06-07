"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    angulo_A = int(input('Digite o ângulo A: '))
    angulo_B = int(input('Digite o ângulo B: '))
    angulo_C = int(input('Digite o ângulo C: '))

    eh_triangulo = verificar_se_triangulo(angulo_A, angulo_B, angulo_C)

    if eh_triangulo:
        tipo_triangulo = obter_tipo_triangulo(angulo_A, angulo_B, angulo_C)
        print(f'É um triangulo {tipo_triangulo}')
    else:
        print('NÃO é um triângulo')


def verificar_se_triangulo(a, b, c):
    condicao_1 = a + b + c == 180
    condicao_2 = a != 0 and b != 0 and c != 0
    return condicao_1 and condicao_2


def obter_tipo_triangulo(a, b, c):
    tipo = ""
    if a > 90 or b > 90 or c > 90:
        tipo = "obtusângulo"
    elif a == 90 or b == 90 or c == 90:
        tipo = "retângulo"
    else:
        tipo = "acutângulo"
    return tipo


main()