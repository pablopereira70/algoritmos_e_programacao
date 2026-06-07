"""
Módulo: 01 - Variáveis e Operadores
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
x2 = int(input('Digite a coordenada x2: '))
x1 = int(input('Digite a coordenada x1: '))
y2 = int(input('Digite a coordenada y2: '))
y1 = int(input('Digite a coordenada y1: '))
#processamento
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) **0.5
#saída
print(f'A distância entre dois pontos no plano corresponde a {d}')