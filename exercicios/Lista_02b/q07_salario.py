"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que calcula o reajuste salarial de um funcionário com base em seu salário atual
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
     salario = float(input('Digite o seu salário(R$): '))

     reajuste = obter_reajuste(salario)
     aumento = obter_aumento(salario, reajuste)
     novo_salario = obter_novo_salario(salario, aumento)

     print(f'''
Salário sem reajuste:  {salario:.2f}
Percentual do aumento: {reajuste}
Valor do aumento:      {aumento:.2f}
Salário com reajuste   {novo_salario:.2f}
''')
     

def obter_reajuste(salario):
    if salario <= 280:
        reajuste = "20%"
    elif salario <= 700:
        reajuste = "15%"
    elif salario <= 1500:
        reajuste = "10%"
    else:
        reajuste = "5%"
    return reajuste


def obter_aumento(salario, reajuste):
    if reajuste == "20%":
        aumento = salario * 0.2
    elif reajuste == "15%":
        aumento = salario * 0.15
    elif reajuste == "10%":
        aumento = salario * 0.1
    else:
        aumento = salario * 0.05
    return aumento


def obter_novo_salario(salario, aumento):
    return salario + aumento


main()