"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que converte uma quantia em dólares para reais com base na cotação.
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