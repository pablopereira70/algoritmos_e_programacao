"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que resolve equações do segundo grau.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    a = int(input('Digite o coeficiente A: '))
    
    if a != 0:
        b = int(input('Digite o coeficiente B: '))
        c = int(input('Digite o coeficiente C: '))
        delta = calcular_delta(a,b,c)
        if delta > 0:
            print('x¹ =',((-b) + delta ** 0.5) / (2 * a))
            print('x² =',((-b) - delta ** 0.5) / (2 * a))
        elif delta == 0:
            print('x¹ e x² =',(-b) / (2 * a))
        else:
            print('Não há solução no conjunto dos reais')
    else:
        print('NÚMERO INVÁLIDO')


def calcular_delta(a,b,c):
    return b ** 2 - 4 * a * c


main()