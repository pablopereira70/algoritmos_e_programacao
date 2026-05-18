"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que calcula a média de duas notas, atribui um conceito e determina o status do aluno (aprovado ou reprovado).
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    nota_1 = float(input('Digite a primeira nota: '))
    nota_2 = float(input('Digite a primeira nota: '))

    media = calcular_media(nota_1, nota_2)
    conceito = obter_conceito(media)
    status = obter_status(conceito)

    print(f'''
Nota(1):  {nota_1}
Nota(2):  {nota_2}
Media:    {media}
Conceito: {conceito}
Status:   {status}
''')


def calcular_media(n1, n2):
    return (n1 + n2) / 2


def obter_conceito(u):
    if u >= 9:
        return 'A'
    elif u >= 7.5:
        return 'B'
    elif u >= 6:
        return 'C'
    elif u >= 4:
        return 'D'
    else:
        return 'E'
    

def obter_status(con):
    if con == 'A' or con == 'B' or con == 'C':
        return 'APROVADO'
    else:
        return 'REPROVADO'


main()