"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    preco_1 = float(input('Digite o primeiro preço: '))
    preco_2 = float(input('Digite o segundo preço: '))
    preco_3 = float(input('Digite o terceiro preço: '))

    mais_barato = obter_mais_barato(preco_1, preco_2, preco_3)

    print(f'O preço mais barato é o R${mais_barato:.2f}')


def obter_mais_barato(p1, p2, p3):
    barato = p1

    if p2 < barato:
        barato = p2
    
    if p3 < barato:
        barato = p3
    
    return barato


main()