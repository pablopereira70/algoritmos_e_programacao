"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que converte uma velocidade de quilômetros por hora (km/h) para metros por segundo (m/s).
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
velocidade_kmh = int(input('Digite um valor(km/h): '))
#processamento
velocidade_ms = velocidade_kmh / 3.6
#saída
print(f'A velocidade {velocidade_kmh}km/h equivale aproximadamente a {velocidade_ms:.2f}m/s')