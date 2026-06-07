"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    num1 = int(input('Digite um número inteiro qualquer: '))
    num2 = int(input('Digite um número inteiro diferente do anterior: '))
    num3 = int(input('Digite um número inteiro diferente dos anteriores: '))
    num4 = int(input('Digite um número inteiro diferente dos anteriores: '))
    num5 = int(input('Digite um número inteiro diferente dos anteriores: '))

    eh_diferente = verificar_se_nums_diferentes(num1, num2, num3, num4, num5)

    if eh_diferente:
        maior_num, menor_num = obter_num_maior_e_menor(num1, num2, num3, num4, num5)
        print(f'O maior número é o {maior_num}')
        print(f'O menor número é o {menor_num}')
    else:
        print('Nem todos os números são diferentes')


def verificar_se_nums_diferentes(n1, n2, n3, n4, n5):
    condicao_1 = n1 != n2 and n1 != n3 and n1 != n4 and n1 != n5
    condicao_2 = n2 != n3 and n2 != n4 and n2 != n5
    condicao_3 = n3 != n4 and n3 != n5
    condicao_4 = n4 != n5
    return condicao_1 and condicao_2 and condicao_3 and condicao_4


def obter_num_maior_e_menor(n1, n2, n3, n4, n5):
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    if n4 > maior:
        maior = n4
    if n5 > maior:
        maior = n5
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    if n4 < menor:
        menor = n4
    if n5 < menor:
        menor = n5
    return maior,menor


main()