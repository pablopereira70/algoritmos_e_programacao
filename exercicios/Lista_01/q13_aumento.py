"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe um valor em reais, calcula um aumento de 70% e exibe o novo valor.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
valor_sem_aumento = float(input('Digite um valor em reais:'))
#processamento
aumento = valor_sem_aumento * 0.70
valor_com_aumento = valor_sem_aumento + aumento
#saída
print(f'A quantia de {valor_sem_aumento}R$ com um aumento de 70% equivale a {valor_com_aumento}R$')