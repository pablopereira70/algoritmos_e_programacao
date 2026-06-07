"""
Módulo: 01 - Variáveis e Operadores
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
valor_min_total = int(input('Digite um valor em minutos: '))
#processamento
valor_h = valor_min_total // 60
valor_min_parcial = valor_min_total % 60
#saída
print(f'{valor_min_total} minutos equivalem a {valor_h} horas e {valor_min_parcial} minutos')