"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe três números, calcula a expressão e exibe o resultado.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
a = int(input('Digite o número A: '))
b = int(input('Digite o número B: '))
c = int(input('Digite o número C: '))
#processamento
r = (a + b) ** 2
s = (b + c) ** 2
d = (r + s) / 2
#saída
print(f'O resultado corresponde a {d}')