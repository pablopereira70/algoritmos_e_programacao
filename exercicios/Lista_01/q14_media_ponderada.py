"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que calcula a média ponderada de três notas com pesos diferentes.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
peso1 = int(input('Digite o peso da primeira nota: '))
peso2 = int(input('Digite o peso da segunda nota: '))
peso3 = int(input('Digite o peso da terceira nota: '))
#processamento
numerador = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)
denominador = peso1 + peso2 + peso3
media_ponderada = numerador / denominador
#saída
print(f'A média ponderada das notas {nota1}, {nota2} e {nota3} de pesos {peso1}, {peso2} e {peso3} respectivamente é igual a {media_ponderada}')