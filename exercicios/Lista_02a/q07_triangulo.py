"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    lado_A = int(input('Digite o lado A: '))
    lado_B = int(input('Digite o lado B: '))
    lado_C = int(input('Digite o lado C: '))
    
    eh_triangulo = verifica_se_triangulo(lado_A, lado_B, lado_C)
    if eh_triangulo:
        tipo_triangulo = obter_tipo_triangulo(lado_A, lado_B, lado_C)
        print(f'É um triângulo {tipo_triangulo}')
    else:
        print('NÃO é um triângulo')

    
def verifica_se_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a


def obter_tipo_triangulo(a, b , c):
    tipo = ''
    if a == b and a == c:
        tipo = 'Equilátero'
    elif a != b and a != c and b != c:
        tipo = 'Escaleno'
    else:
        tipo = 'Isósceles'
    return tipo


main()