"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que calcula a área de um retângulo.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    x1 = int(input('Digite a coordenada x¹: '))
    y1 = int(input('Digite a coordenada y¹: '))
    x2 = int(input('Digite a coordenada x²: '))
    y2 = int(input('Digite a coordenada y²: '))

    area = calcular_area(x1,y1,x2,y2)
    
    print(f'Área do retângulo = {area}')


def calcular_area(x1,y1,x2,y2):
    base = x2 - x1
    altura = y2 - y1
    return base * altura


main()