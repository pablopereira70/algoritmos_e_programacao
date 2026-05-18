"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que verifica se um número de 4 dígitos é um quadrado perfeito.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    numero = int(input('Digite um número de 4 dígitos: '))

    eh_quadrado_perfeito = verificar_eh_quadrado_perfeito(numero)
    
    if eh_quadrado_perfeito:
        print(f'SIM. o número {numero} é um quadrado perfeito')
    else:
        print(f'NÃO. o número {numero} não é um quadrado perfeito')


def verificar_eh_quadrado_perfeito(num):
    par_1 = num // 100
    par_2 = num % 100
    return par_1 + par_2 == num ** 0.5


main()