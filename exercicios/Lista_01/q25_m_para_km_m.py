"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe um valor em metros, converte para quilômetros e metros, e exibe o resultado.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
valor_m_total = int(input('Digite um valor(m): '))
#processamento
valor_km = valor_m_total // 1000
valor_m_parcial = valor_m_total % 1000
#saída
print(f'O valor de {valor_m_total}m corresponde a {valor_km}km e {valor_m_parcial}m')