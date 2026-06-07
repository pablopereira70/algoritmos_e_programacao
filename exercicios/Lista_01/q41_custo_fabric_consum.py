"""
Módulo: 01 - Variáveis e Operadores
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
custo_total = float(input('Digite o custo total do veículo: '))
#processamento
custo_fabrica = custo_total * (100/173)
custo_consumidor = custo_total * (73/173)
#saída
print(f'O custo de fábrica corresponde a: {custo_fabrica:.2f}')
print(f'O custo do consumidor corresponde a: {custo_consumidor:.2f}')