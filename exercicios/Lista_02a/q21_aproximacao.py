"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que aproxima um número real para o inteiro mais próximo.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    numero = float(input("Digite um número real qualquer: "))

    numero_aprox = obter_aproximacao(numero)
    
    print(f'O número aproximado corresponde: {numero_aprox}')


def obter_aproximacao(n):
    parte_inteira = n // 1
    parte_fracionaria = n % 1
    if parte_fracionaria >= 0.5:
        return parte_inteira + 1
    else:
        return parte_inteira
    

main()