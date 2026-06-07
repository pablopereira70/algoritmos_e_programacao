"""
Módulo: 01 - Variáveis e Operadores
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