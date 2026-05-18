"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que converte horas e minutos para minutos totais.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
valor_h = int(input('Digite o valor em horas: '))
valor_min = int(input('Digite o valor em minutos: '))
#processamento
soma_min = valor_h * 60 + valor_min
#saída
print(f'{valor_h} horas e {valor_min} minutos equivalem a {soma_min} minutos')