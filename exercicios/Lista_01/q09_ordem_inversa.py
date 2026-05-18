"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe dois números do usuário e exibe os números em ordem inversa.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
a = int(input('Digite o número A: '))
b = int(input('Digite o número B: '))
#processamento
temp = a
a = b
b = temp
#saída
print(f'{a} {b}')