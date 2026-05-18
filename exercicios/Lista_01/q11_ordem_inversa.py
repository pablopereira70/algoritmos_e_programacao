"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe um número inteiro de três algarismos do usuário e exibe os algarismos em ordem inversa.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
numero = int(input('Digite um número inteiro de três algarismos:'))
#processamento
algarismo_1 = numero // 100
algarismo_2 = (numero % 100) // 10
algarismo_3 = (numero % 100) % 10
#saída
print(f'O número {numero} em ordem inversa é igual a {algarismo_3}{algarismo_2}{algarismo_1}')