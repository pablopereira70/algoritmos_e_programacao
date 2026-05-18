"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe três números do usuário, calcula a soma dos dois primeiros e a diferença dos dois últimos, e exibe os resultados.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
terceiro_numero = int(input('Digite o terceiro número: '))
#processamento
soma_2primeiros = primeiro_numero + segundo_numero
diferença_2ultimos = segundo_numero - terceiro_numero
#saída
print(f'A soma dos dois primeiros números é igual a {soma_2primeiros} e a diferença dos dois últimos equivale a {diferença_2ultimos}')