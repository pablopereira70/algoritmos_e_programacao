"""
Módulo: 01 - Variáveis e Operadores
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
binario = int(input('Digite um número binário(4 dígitos): '))
#processamento
digito_4 = binario // 1000
digito_3 = (binario % 1000) // 100
digito_2 = ((binario % 1000) % 100) // 10
digito_1 = ((binario % 1000) % 100) % 10
decimal = (digito_4 * 8) + (digito_3 * 4) + (digito_2 * 2) + (digito_1 * 1)
#saída
print(f'O número binário {digito_4}{digito_3}{digito_2}{digito_1} corresponde a {decimal} na base decimal')