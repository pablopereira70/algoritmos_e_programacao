"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que calcula a soma dos algarismos de um número de três dígitos.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
numero_3alg = int(input('Digite um número de três algarismos:'))
#processamento
centena = numero_3alg // 100
dezena = (numero_3alg % 100) // 10
unidade = (numero_3alg % 100) % 10
soma_3alg = centena + dezena + unidade
#saída
print(f'A soma dos três algarismos do número {numero_3alg} é igual a {soma_3alg}')