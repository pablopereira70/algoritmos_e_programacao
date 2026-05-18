"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe um número de três algarismos, inverte a ordem dos algarismos, calcula a soma entre o número original e o número invertido, e exibe o resultado.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
numero_3algarismos = int(input('Digite um número de três algarismos: '))
#processamento
unidade = numero_3algarismos // 100
dezena = (numero_3algarismos % 100) // 10
centena = (numero_3algarismos % 100) % 10
numero_inverso = (centena * 100) + (dezena * 10) + (unidade)
soma = numero_3algarismos + numero_inverso
#saída
print(f'A soma entre {numero_3algarismos} e {numero_inverso} corresponde a {soma}')