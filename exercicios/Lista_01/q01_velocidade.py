"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que converte uma velocidade de metros por segundo (m/s) para quilômetros por hora (km/h).
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
velocidade_ms = int(input('Digite um valor(m/s): '))
#processamento
velocidade_kmh = velocidade_ms * 3.6
#saída
print(f'A velocidade {velocidade_ms}m/s equivale aproximadamente a {velocidade_kmh:.2f}km/h')