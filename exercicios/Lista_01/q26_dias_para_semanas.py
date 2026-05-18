"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe um valor em dias, converte para semanas e dias, e exibe o resultado.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
valor_dias_total = int(input('Digite um valor(dias): '))
#processamento
valor_semanas = valor_dias_total // 7
valor_dias_parcial = valor_dias_total % 7
#saída
print(f'O valor de {valor_dias_total} dia(s) corresponde a {valor_semanas} semana(s) e {valor_dias_parcial} dia(s)')