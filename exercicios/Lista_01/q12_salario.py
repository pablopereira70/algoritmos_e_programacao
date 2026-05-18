"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe o salário de um trabalhador, calcula um aumento de 25% e exibe o novo salário.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
salario_sem_aumento = float(input('digite o salário de um trabalhador:'))
#processamento
aumento = salario_sem_aumento * 0.25
salario_com_aumento = salario_sem_aumento + aumento
#saída
print(f'o salário de {salario_sem_aumento} com um aumento de 25% equivale a {salario_com_aumento}')