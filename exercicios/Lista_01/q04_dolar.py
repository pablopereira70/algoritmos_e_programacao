"""
Módulo: 01 - Variáveis e Operadores
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
valor_cotaçao = float(input('Digite a cotação do dólar: '))
valor_dólar = float(input('Digite uma quantia em dólares: '))
#processamento
valor_real = (valor_dólar * valor_cotaçao)
#saída
print(f'{valor_dólar} dólares equivalem a aproximadamente {valor_real :.2f} reais')