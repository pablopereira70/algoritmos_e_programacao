"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    total_aprovados, total_reprovados, total_alunos = ler_info_alunos()

    print("---------INFORMAÇÕES---------")
    print(f"Total de aprovados:  {total_aprovados}")
    print(f"Total de reprovados: {total_reprovados}")
    print(f"Total de alunos:     {total_alunos}")


def ler_info_alunos():
    reprovados = 0
    aprovados = 0
    alunos = 0

    while True:
        matricula = obter_inteiro("Digite o número da matrícula: ")

        if matricula == 0:
            break

        alunos += 1
        nota1, nota2, nota3 = ler_notas(alunos)
        media = calcular_media(nota1, nota2, nota3)

        if media >= 7:
            aprovados += 1
        else:
            reprovados += 1
        
    return aprovados, reprovados, alunos


def ler_notas(alunos):
    print(f"{alunos}º ALUNO")
    n1 = obter_nota("Digite a primeira nota: ")
    n2 = obter_nota("Digite a segunda nota: ")
    n3 = obter_nota("Digite a terceira nota: ")
    return n1, n2, n3


def calcular_media(n1, n2, n3):
    return (2 * n1 + 3 * n2 + 5 * n3) / 10


def obter_nota(conteudo):
    while True:
        try:
            nota = obter_real(conteudo)
            if nota >= 0 and nota <= 10:
                return nota
            erro = 1 / 0
        except:
            exibir("Valor inválido. Digite um valor no intervalo de 0 a 10")


main()