"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que verifica o status de aprovação de um aluno com base em suas notas.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    nota_1 = float(input('Digite a primeira nota: '))
    nota_2 = float(input('Digite a segunda nota: '))
    media = calcular_media(nota_1, nota_2)
    if media >= 7:
        print('APROVADO')
    elif media == 10:
        print('APROVADO COM DISTINÇÃO')
    else:
        print('REPROVADO')


def calcular_media(n1, n2):
    return (n1 + n2) / 2


main()