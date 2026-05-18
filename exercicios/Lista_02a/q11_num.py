"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que exibe o número correspondente à opção escolhida pelo usuário.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main(): 
    opcao = int(input('Digite um dos números listados(1,2,3): '))
    if opcao == 3 or opcao == 2 or opcao == 1:
        num1 = int(input('Digite um número inteiro qualquer: '))
        num2 = int(input('Digite um número inteiro qualquer: '))
        num3 = int(input('Digite um número inteiro qualquer: '))

        num_escolhido = verificar_num_escolhido(opcao, num1, num2, num3)

        print(num_escolhido)
    else:
        print('Esse número é inválido')


def verificar_num_escolhido(p,n1,n2,n3):
    if p == 1:
        return n1
    elif p == 2:
        return n2
    else:
        return n3
    

main()