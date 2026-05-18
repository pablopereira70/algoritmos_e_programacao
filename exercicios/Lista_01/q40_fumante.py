"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe há quantos anos fuma, quantos cigarros fuma por dia, o preço da carteira de cigarro, calcula a quantia gasta com cigarros em um ano, e exibe o resultado.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
anos_fuma = int(input('Digite há quantos anos fuma: '))
cigarros_dia = int(input('Digite quantos cigarros fuma por dia: '))
preco_carteira = float(input('Digite o preço da carteira de cigarro: '))
#processamento
cigarros_total = anos_fuma * 365 * cigarros_dia
quantidade_carteira = cigarros_total / 20
dinheiro_gasto = quantidade_carteira * preco_carteira
#saída
print(f'A quantia gasta com cigarros em {anos_fuma} ano(s) corresponde a {dinheiro_gasto:.2f}')