"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe a base e a altura de um triângulo, calcula a área do triângulo e exibe o resultado.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
base_triangulo = int(input('Digite a base do triângulo:'))
altura_triangulo = int(input('Digite a altura do triângulo'))
#processamento
area_triangulo = base_triangulo * altura_triangulo / 2
#saída
print(f'O triângulo de base {base_triangulo} e altura {altura_triangulo} tem área igual a {area_triangulo}')