"""
Módulo: 01 - Variáveis e Operadores
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
a = int(input('Digite o coeficiente A: '))
b = int(input('Digite o coeficiente B: '))
c = int(input('Digite o coeficiente C: '))
d = int(input('Digite o coeficiente D: '))
e = int(input('Digite o coeficiente E: '))
f = int(input('Digite o coeficiente F: '))
#processamento
x = (c * e - b * f) / (a * e - b * d)
y = (a * f - c * d) / (a * e  - b * d)
#saída
print(f'x = {x}')
print(f'y = {y}')