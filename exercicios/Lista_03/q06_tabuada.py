"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    for i in range(1, 11):
        escrever_tabuada(i)

  
def escrever_tabuada(n):
    print("  ADIÇÃO   \t   SUBTRAÇÃO   \t   DIVISÃO   \t   MULTIPLICAÇÃO  ")
    for i in range(1, 11):
        adi = i + n
        sub = (n + i) - n
        div = (n * i) / n
        mul = i * n
        print(f"{i} + {n} = {adi} \t {n + i} - {n} = {sub} \t {n * i} / {n} = {div:.1f} \t {i} * {n} = {mul}")


main()