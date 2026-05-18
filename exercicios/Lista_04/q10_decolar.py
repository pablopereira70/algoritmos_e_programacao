"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para calcular o peso total de um avião e verificar se ele pode decolar
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    quant_conteiners = obter_inteiro("Digite a quantidade de conteiners: ")
    peso_conteiners = obter_peso_conteiners(quant_conteiners)
    quant_passageiros, quant_bagagem = ler_dados_passageiros()

    peso_passageiros = obter_peso_passageiros(quant_passageiros, quant_bagagem)
    quant_combustivel = 10000
    peso_combustivel = obter_peso_combustivel(quant_combustivel)
    pode_decolar = verificar_se_pode_decolar(peso_conteiners, peso_combustivel, peso_passageiros)
    quant_combustivel = ajustar_quant_combustivel(peso_combustivel, peso_conteiners, peso_passageiros)

    print("-----------------INFORMAÇÕES-----------------")
    print(f"Quantidade de passageiros: {quant_passageiros}")
    print(f"Quantidade de bagagens:    {quant_bagagem}")
    print(f"Peso dos passageiros:      {peso_passageiros}kg")
    print(f"Peso da carga:             {peso_conteiners}kg")
    print(f"Quantidade de combustível: {quant_combustivel:.0f}L")
    print(f"Liberado para decolagem:   {pode_decolar}")


def ler_dados_passageiros():
    quant_passageiros = 0
    quant_total_bagagem = 0

    while True:
        num_bilhete = obter_inteiro("Digite o número do bilhete: ")

        if num_bilhete == 0:
            break

        quant_bagagem = obter_inteiro("Digite a quantidade de bagagens: ")

        quant_passageiros += 1
        quant_total_bagagem += quant_bagagem

    return quant_passageiros, quant_total_bagagem


def obter_peso_conteiners(n):
    peso_total = 0
    for i in range(n):
        peso = obter_inteiro(f"Digite o peso do {i + 1}º conteiner(kg): ")
        peso_total += peso
    return peso_total


def obter_peso_passageiros(q1, q2):
    return q1 * 70 + q2 * 10


def obter_peso_combustivel(quant):
    return quant * 1.5

def verificar_se_pode_decolar(p1, p2, p3):
    peso_total = p1 + p2 + p3

    if peso_total > 500000:
        return "não"
    else:
        return "sim"
    

def ajustar_quant_combustivel(p1, p2, p3):
    peso_total = p1 + p2 + p3

    if 500000 - peso_total >= 0:
        add = (500000 - peso_total) / 1.5
        return 10000 + add
    else:
        rem = (500000 - peso_total) / 1.5
        return 10000 + rem


main()