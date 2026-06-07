"""
Módulo: 01 - Variáveis e Operadores
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
ano = int(input('Digite sua idade em anos: '))
mes = int(input('Digite a sua idade em meses: '))
dia_parcial = int(input('Digite a sua idade em dias: '))
#processamento
dia_total = (ano * 365) + (mes * 30) + dia_parcial
#saída
print(f'A sua idade em dias é igual a {dia_total}')