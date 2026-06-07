"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    num1 = int(input('Digite um número inteiro qualquer: '))
    num2 = int(input('Digite um número inteiro qualquer: '))
    
    resto = num1 % num2
    if resto == 1:
        soma = num1 + num2 + resto
        print(soma)
    elif resto == 2:
        if num1 % 2 == 0:
            print(f'{num1} é par')
        else:
            print(f'{num1} é ímpar')
        if num2 % 2 == 0:
            print(f'{num2} é par')
        else:
            print(f'{num2} é ímpar') 
    elif resto == 3:
        soma = num1 + num2
        print(soma * num1)
    elif resto == 4 and num2 != 0:
        soma = num1 + num2
        print(soma / num2)
    else:
        print(num1 ** 2)
        print(num2 ** 2)


main()