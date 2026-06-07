"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    h_prof1 = int(input("Digite quantas horas o professor 1 trabalha: "))
    h_prof2 = int(input("Digite quantas horas o professor 2 trabalha: "))
    valor_h_prof1 = float(input('Digite o valor da hora do professor 1: '))
    valor_h_prof2 = float(input('Digite o valor da hora do professor 2: '))
    
    escrever_maior_salario(h_prof1, valor_h_prof1, h_prof2, valor_h_prof2)


def escrever_maior_salario(h1, valor_h1, h2, valor_h2):
    salario_prof1 = h1 * valor_h1
    salario_prof2 = h2 * valor_h2
    if salario_prof1 > salario_prof2:
        print('O professor 1 tem o maior salário total')
    elif salario_prof2 > salario_prof1:
        print('O professor 2 tem o maior salário total')
    else:
        print('Os professores tem o mesmo salário total')


main()