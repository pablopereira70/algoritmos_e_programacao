"""
Módulo: 01 - Variáveis e Operadores
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
numero_4algarismos = int(input('Digite um número de quatro algarismos: '))
#processamento
digito_4 = numero_4algarismos // 1000
digito_3 = (numero_4algarismos % 1000) // 100
digito_2 = ((numero_4algarismos % 1000) % 100) // 10
digito_1 = ((numero_4algarismos % 1000) % 100) % 10
soma_digitos = digito_4 + digito_3 + digito_2 + digito_1
#saída
print(f'A soma dos algarismos do número {numero_4algarismos} corresponde a {soma_digitos}')