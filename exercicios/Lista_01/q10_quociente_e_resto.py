"""
Disciplina: Algoritmos e Programação
Módulo: 01 - Variáveis e Operadores
Descrição: Programa que recebe dois números do usuário, calcula o quociente e o resto da divisão do primeiro número pelo segundo, e exibe os resultados.
Autor: Pablo Pereira
Data: Maio / 2026
"""

#entrada
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
#processamento
quociente = n1 / n2
resto = n1 % n2
#saída
print(f'O quociente e o resto dos números {n1} e {n2} são respectivamente {quociente} e {resto}')