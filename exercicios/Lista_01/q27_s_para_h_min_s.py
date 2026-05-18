"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe um valor em segundos, converte para horas, minutos e segundos, e exibe o resultado.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
valor_s_total = int(input('Digite um valor(s): '))
#processamento
temporario_min = valor_s_total // 60
valor_s = valor_s_total % 60
valor_h = temporario_min // 60
valor_min = temporario_min % 60
#saída
print(f'O valor de {valor_s_total}s corresponde a {valor_h}h, {valor_min}min e {valor_s}s')