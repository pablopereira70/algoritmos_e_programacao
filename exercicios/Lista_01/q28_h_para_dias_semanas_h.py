"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe um valor em horas, converte para semanas, dias e horas, e exibe o resultado.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
valor_h_total = int(input('Digite um valor(h): '))
#processamento
temporario_dias = valor_h_total // 24
valor_h_parcial = valor_h_total % 24
valor_semana = temporario_dias // 7
valor_dia = temporario_dias % 7
#saída
print(f'O valor de {valor_h_total}h corresponde a {valor_semana} semana(s), {valor_dia} dia(s) e {valor_h_parcial}h')