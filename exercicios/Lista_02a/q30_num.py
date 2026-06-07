"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    numero = int(input('Digite um número de 4 dígitos: '))

    obedece_regra = verificar_obedece_regra(numero)
    
    if obedece_regra:
        print(f'SIM. o número {numero} obedece a regra.')
    else:
        print(f'NÃO. o número {numero} não obedece a regra.')


def verificar_obedece_regra(num):
    par_1 = num // 100
    par_2 = num % 100
    return (par_1 + par_2) ** 2 == num


main()