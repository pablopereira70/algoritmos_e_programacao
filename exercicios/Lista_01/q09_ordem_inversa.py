"""
Módulo: 01 - Variáveis e Operadores
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