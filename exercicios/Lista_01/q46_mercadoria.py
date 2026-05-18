"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe o valor de uma mercadoria, calcula o valor da entrada e das parcelas para um pagamento em 3 vezes, e exibe os resultados. 
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
valor_mercadoria = float(input('Digite o valor da mercadoria: '))
#processamento
valor_parcela = valor_mercadoria // 3
valor_entrada = valor_mercadoria - 2 * valor_parcela
#saída
print(f'A entrada corresponde a {valor_entrada}R$')

print(f'As parcelas correspondem {valor_parcela}R$')