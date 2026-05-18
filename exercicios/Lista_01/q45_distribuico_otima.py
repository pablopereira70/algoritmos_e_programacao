"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe a quantia desejada, calcula a distribuição ótima de notas para essa quantia, e exibe os resultados.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
valor_solicitado = float(input('Digite a quantia desejada(R$): '))
#processamento
nota_200 = valor_solicitado // 200
resto_200 = valor_solicitado % 200
nota_100 = resto_200 // 100
resto_100 = resto_200 % 100
nota_50 = resto_100 // 50
resto_50 = resto_100 % 50
nota_20 = resto_50 // 20
resto_20 = resto_50 % 20
nota_10 = resto_20 // 10
resto_10 = resto_20 % 10
nota_5 = resto_10 // 5
resto_5 = resto_10 % 5
nota_2 = resto_5 // 2
resto_2 = resto_5 % 2
nota_1 = resto_2
#saída
print('A distribuição de notas corresponde a: ')
print(f'{nota_200} notas de 200R$')
print(f'{nota_100} notas de 100R$')
print(f'{nota_50} notas de 50R$')
print(f'{nota_20} notas de 20R$')
print(f'{nota_10} notas de 10R$')
print(f'{nota_5} notas de 5R$')
print(f'{nota_2} notas de 2R$')
print(f'{nota_1} notas de 1R$')