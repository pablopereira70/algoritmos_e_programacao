"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que verifica o sexo de uma pessoa a partir de uma letra (F ou M).
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    letra = input('Digite uma letra qualquer(maiúscula): ')
    if letra == 'F':
        print('Feminino')
    elif letra == 'M':
        print('Masculino')
    else:
        print("Sexo inválido")


main()