"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    peso = int(input('Digite o seu peso(kg): '))
    altura = float(input('Digite a sua altura(m): '))

    imc = calcular_imc(peso,altura)
    
    if imc < 25:
        print('Peso normal')
    elif imc < 30:
        print('Obeso')
    else:
        print('Obesidade mórbida')


def calcular_imc(kg,m):
    return kg / m ** 2


main()