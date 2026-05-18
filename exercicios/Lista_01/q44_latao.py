"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe a quantidade de latão que se quer obter, calcula a quantidade de cobre e zinco necessária para obter essa quantidade de latão, e exibe os resultados.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
latao = int(input('Digite a quantidade de latão que se quer obter(kg): '))
#processamento
cobre = latao * 0.7
zinco = latao * 0.3
#saída
print(f'Para obter {latao}kg de latão necessita-se de {cobre}kg de cobre e de {zinco}kg de zinco')