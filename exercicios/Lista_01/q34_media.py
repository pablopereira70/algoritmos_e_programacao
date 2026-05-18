"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe três números, calcula a média e exibe o resultado.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
numero_3 = int(input('Digite o terceiro número: '))
#processamento
media = (numero_1 + numero_2 + numero_3) / 3
#saída
print(f'A média dos números {numero_1}, {numero_2} e {numero_3} corresponde a {media:.2f}')