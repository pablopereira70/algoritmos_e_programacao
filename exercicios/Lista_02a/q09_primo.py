"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    numero = int(input('Digite um número entre 0 a 100: '))
    
    if 0 < numero and numero < 100:
        if numero != 1:
            nao_primo = verificar_se_nao_primo(numero)
            if nao_primo:
                print('NÃO é um número primo')
            else:
                print('É um numero primo')
        else:
            print('NÃO é um número primo')
    else:
        print('ESSE NÚMERO NÃO É VÁLIDO')
    

def verificar_se_nao_primo(n):
    return (n % 2 == 0 and n != 2) or (n % 3 == 0 and n != 3) or (n % 5 == 0 and n != 5) or (n % 7 == 0 and n != 7)


main()