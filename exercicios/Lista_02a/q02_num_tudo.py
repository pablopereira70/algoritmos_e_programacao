"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))

    maior_numero, menor_numero = obter_maior_e_menor_numero(numero_1, numero_2)
    
    if maior_numero != menor_numero:
        print(f'O maior número é o {maior_numero}')
        print(f'O menor número é o {menor_numero}')
    else:
        print('Os números são iguais')


def obter_maior_e_menor_numero(n1, n2):
    maior, menor = n1, n2
    if maior < menor:
        maior, menor = n2, n1
    return maior, menor


main()