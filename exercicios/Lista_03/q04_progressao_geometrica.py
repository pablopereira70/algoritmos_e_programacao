"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    inicial = int(input('Digite o primeiro termo: '))
    limite = int(input('Digite o limite: '))
    razao = int(input('Digite a razão: '))

    num = inicial
    print(inicial)
    while True:
        num *= razao
        if num >= limite:
            break
        print(num)


main()