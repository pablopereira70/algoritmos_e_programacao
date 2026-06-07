"""
Módulo: 01 - Variáveis e Operadores
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
diferenca = numero_3algarismos - numero_inverso
#saída
print(f'A diferença entre {numero_3algarismos} e {numero_inverso} corresponde a {diferenca}')