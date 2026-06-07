"""
Módulo: 01 - Variáveis e Operadores
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
velocidade_kmh = int(input('Digite um valor(km/h): '))
#processamento
velocidade_ms = velocidade_kmh / 3.6
#saída
print(f'A velocidade {velocidade_kmh}km/h equivale aproximadamente a {velocidade_ms:.2f}m/s')