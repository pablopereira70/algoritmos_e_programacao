"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: ')) 

    div = 0
    for n in range(limite_inferior, limite_superior):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                div += 1
                break
        if div == 0:
            print(n)
        div = 0


main()