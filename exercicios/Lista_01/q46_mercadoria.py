"""
Módulo: 01 - Variáveis e Operadores
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