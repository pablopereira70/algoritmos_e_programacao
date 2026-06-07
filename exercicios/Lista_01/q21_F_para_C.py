"""
Módulo: 01 - Variáveis e Operadores
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
temperatura_fahrenheit = int(input('Digite a temperatura em fahrenheit: '))
#processamento
temperatura_celsius = (5 * temperatura_fahrenheit - 160) / 9
#saída
print(f'A temperatura de {temperatura_fahrenheit}°F equivale a {temperatura_celsius}°C')