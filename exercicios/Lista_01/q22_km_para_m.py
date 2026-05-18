"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe uma medida em quilômetros, converte para metros, e exibe o resultado.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
medida_km = int(input('Digite uma medida em km: '))
#processamento
medida_m = medida_km * 1000
#saída
print(f'A medida de {medida_km}km equivale a {medida_m}m')