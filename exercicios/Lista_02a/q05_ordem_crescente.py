"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))
    numero_3 = int(input('Digite o terceiro número: '))

    numero_1, numero_2, numero_3 = obter_ordem_crescente(numero_1, numero_2, numero_3)
    
    print(f'({numero_1},{numero_2},{numero_3})')


def obter_ordem_crescente(n1, n2, n3):
    primeiro, segundo, terceiro = n3, n2, n1
    if terceiro < segundo:
        terceiro, segundo = segundo, terceiro
    if terceiro < primeiro:
        terceiro, primeiro = primeiro, terceiro
    if segundo < primeiro:
        segundo, primeiro = primeiro, segundo
    return primeiro, segundo, terceiro


main()