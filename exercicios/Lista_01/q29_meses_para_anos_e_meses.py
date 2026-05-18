"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe um valor em meses, converte para anos e meses, e exibe o resultado.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
meses_total = int(input('Digite um valor(meses): '))
#processamento
anos = meses_total // 12
meses_parcial = meses_total % 12
#saída
print(f'{meses_total} meses correspondem a {anos} ano(s) e {meses_parcial} meses')