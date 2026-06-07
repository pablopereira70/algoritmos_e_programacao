"""
Módulo: 01 - Variáveis e Operadores
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
numerador_1 = int(input('Digite o numerador da 1º fração: '))
denominador_1 = int(input('Digite o denominador da 1º fração: '))
numerador_2 = int(input('Digite o numerador da 2º fração: '))
denominador_2 = int(input('Digite o denominador da 2º fração: '))
#processamento
numerador_final = (numerador_1 * denominador_2) + (numerador_2 * denominador_1)
denominador_final = denominador_1 * denominador_2
#saída
print(f'A soma das frações corresponde a {numerador_final}/{denominador_final}')