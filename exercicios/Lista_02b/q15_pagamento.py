"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que calcula o valor a ser pago por um cliente em uma fruteira
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    quant_maca = int(input('Digite a quantidade de maça(kg): '))
    quant_morango = int(input('Digite a quantidade de morango(kg): '))

    custo_maca = obter_custo_maca(quant_maca)
    custo_morango = obter_custo_morango(quant_morango)
    total_custo = custo_maca + custo_morango
    desc = obter_desc(total_custo, quant_maca, quant_morango)
    valor_client = total_custo - desc

    print(f'Conta: R${valor_client:.2f}')


def obter_custo_maca(kg):
    if kg > 5:
        return kg * 1.5
    else:
        return kg * 1.8
    

def obter_custo_morango(kg):
    if kg > 5:
        return kg * 2.2
    else:
        return kg * 2.5
    

def obter_desc(total_reais, maca_kg, morango_kg):
    if total_reais >= 25 or (maca_kg + morango_kg) > 8:
        return total_reais * 0.1
    else:
        return 0
    

main()