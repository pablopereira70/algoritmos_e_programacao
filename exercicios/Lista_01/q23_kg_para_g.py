"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe um valor em quilogramas, converte para gramas, e exibe o resultado.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
valor_kg = int(input('Digite uma valor(kg): '))
#processamento
valor_g = valor_kg * 1000
#saída
print(f'O valor de {valor_kg}kg equivale a {valor_g}g')