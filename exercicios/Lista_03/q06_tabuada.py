"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que imprime a tabuada de 1 a 10.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    for i in range(1, 11):
        escrever_tabuada(i)

  
def escrever_tabuada(n):
    print("----------------------------------------------------------------------------------")
    for i in range(1, 11):
        adi = i + n
        sub = (n + i) - n
        div = (n * i) / n
        mul = i * n
        print(f"{i} + {n} = {adi} \t {n + i} - {n} = {sub} \t {n * i} / {n} = {div:.2f} \t {i} * {n} = {mul}")


main()