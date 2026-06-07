"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    pontuacao_A, pontuacao_B = ler_info()

    vencedor = determinar_vencedor(pontuacao_A, pontuacao_B)

    print("---PONTUAÇÃO---")
    print(f"Clube A:  {pontuacao_A}")
    print(f"Clube B:  {pontuacao_B}")
    print(f"Vencedor: {vencedor}")


def ler_dados_nadador(i):
    print(i + 1,"º NADADOR")
    nome = obter_texto("Digite seu nome: ")
    classif = obter_inteiro_positivo("Digite sua classificação(1,2,3,...): ")
    tempo = obter_texto("Digite seu tempo(h:mm): ")
    clube = obter_clube("Digite seu clube(A ou B): ")
    return classif, clube


def determinar_vencedor(a, b):
    if a > b:
        return "Clube A"
    elif b > a:
        return "Clube B"
    else:
        return "Empate"
    

def calcular_pontos_ganhos(pos):
    if pos == 1:
        return 9
    elif pos == 2:
        return 6
    elif pos == 3:
        return 4
    elif pos == 4:
        return 3
    else:
        return 0
    

def ler_info():
    pontos_A = 0
    pontos_B = 0

    while True:
        num_prova = obter_inteiro("Digite o número da prova: ")
        quant_nadadores = obter_inteiro("Digite a quantidade de nadadores: ")

        if num_prova == 0 and quant_nadadores == 0:
            break

        pontos_A, pontos_B = ler_dados_nadadores(quant_nadadores, pontos_A, pontos_B)

    return pontos_A, pontos_B


def ler_dados_nadadores(quant, a, b):
    pont_a = a
    pont_b = b

    for i in range(quant):
            classif, clube = ler_dados_nadador(i)
            pontos_ganhos = calcular_pontos_ganhos(classif)
            
            if clube == "A" or clube == "a":
                pont_a += pontos_ganhos
            else:
                pont_b += pontos_ganhos

    return pont_a, pont_b

def obter_clube(conteudo):
    while True:

        try:
            clube = obter_texto(conteudo)

            if clube == 'A' or clube == 'a' or clube == 'b' or clube ==  'B':
                return clube
            
            erro = 1 / 0
        except:
            exibir('Esse clube não existe. somente A ou B')


main()