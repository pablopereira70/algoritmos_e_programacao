"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que calcula a divisão da soma pela subtração de dois números.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
#processamento
soma_dos_2numeros = numero1 + numero2
subtraçao_dos_2numeros = numero1 - numero2
divisao = soma_dos_2numeros / subtraçao_dos_2numeros
#saída
print(f'A divisão da soma pela subtração dos números {numero1} e {numero2} é igual a {divisao}')