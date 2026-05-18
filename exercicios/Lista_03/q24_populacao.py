"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que lê a quantidade de habitantes de uma população, e depois para cada habitante, lê o salário e o número de filhos. O programa deve calcular e exibir: a média do salário da população, a média do número de filhos, e o percentual de pessoas com salário até 1000.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    n = int(input('Digite a quantidade de habitantes: '))

    soma_salarios = 0
    soma_filhos = 0
    quant_1000 = 0
    for i in range(n):
        num_salario = int(input('Digite o salário: '))
        num_filho = int(input('Digite o número de filhos: '))
        if num_salario <= 1000:
            quant_1000 += 1
        soma_salarios += num_salario
        soma_filhos += num_filho

    print(f'Média do salários da população: {soma_salarios/n:.2f}')
    print(f'Média do número de filhos: {soma_filhos/n}')
    print(f'Percentual de pessoas com salário até 1000: {(quant_1000/n)*100:.1f}%')


main()