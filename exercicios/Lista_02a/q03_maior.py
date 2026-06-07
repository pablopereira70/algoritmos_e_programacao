"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))
    numero_3 = int(input('Digite o terceiro número: '))

    maior_numero = obter_maior_numero(numero_1, numero_2, numero_3)
    
    print(f'O maior número é o {maior_numero}')


def obter_maior_numero(n1, n2, n3):
    maior = n1
    if maior < n2:
        maior = n2
    if maior < n3:
        maior = n3
    return maior


main()