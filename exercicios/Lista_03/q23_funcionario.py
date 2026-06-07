"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    n = int(input('Digite a quantidade de fichas: '))

    f = 0
    for i in range(n):
        f += 1
        codigo = input('Digite o código do funcionário: ')
        num_ht = int(input('Digite a quantidade de horas trabalhadas: '))
        num_dep = int(input('Digite o número de dependentes: '))

        salario_bruto = num_ht * 12 + num_dep * 40
        inss = salario_bruto * 0.085
        ir = salario_bruto * 0.05
        total_desconto = ir + inss
        salario_liquido = salario_bruto - total_desconto

        print(f'FUNCIONÁRIO {f}')
        print(f'Código:          {codigo}')
        print(f'Salário bruto:   {salario_bruto:.2f}')
        print(f'INSS:            {inss:.2f}')
        print(f'IR:              {ir:.2f}')
        print(f'Salário líquido: {salario_liquido:.2f}')


main()