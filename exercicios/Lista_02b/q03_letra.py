"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que verifica se uma letra é uma vogal ou consoante.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    letra = input('Digite uma letra qualquer(maiúscula): ')
    if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        print(f'A letra {letra} é uma vogal')
    else:
        print(f'A letra {letra} é uma cosoante')


main()