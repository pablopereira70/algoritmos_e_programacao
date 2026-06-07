"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    valor_h = int(input('Digite  o valor da sua hora(R$/h): '))
    quant_h = int(input('Digite a quantidade de horas trabalhadas: '))

    salario_bruto = obter_salario_bruto(valor_h, quant_h)
    imp_renda = obter_imp_renda(salario_bruto)
    inss = obter_inss(salario_bruto)
    fgts = obter_fgts(salario_bruto)
    total_desc = obter_total_desc(imp_renda, inss)
    salario_liquido = obter_salario_liquido(salario_bruto, total_desc)

    print(f'''
Salário bruto:      {salario_bruto:.2f}
IR:                 {imp_renda:.2f}
INSS:               {inss:.2f}
FGTS:               {fgts:.2f}
Total de descontos: {total_desc:.2f}
Salário líquido:    {salario_liquido:.2f}
''')
    

def obter_salario_bruto(valor_h, quant_h):
    return valor_h * quant_h


def obter_imp_renda(salario_bruto):
    if salario_bruto > 2500:
        imposto = salario_bruto * 0.2
    elif salario_bruto > 1500:
        imposto = salario_bruto * 0.1
    elif salario_bruto > 900:
        imposto = salario_bruto * 0.05
    else:
        imposto = 0
    return imposto


def obter_inss(salario_bruto):
    return salario_bruto * 0.1


def obter_fgts(salario_bruto):
    return salario_bruto * 0.11


def obter_total_desc(ir, inss):
    return ir + inss


def obter_salario_liquido(salario_bruto, total_desc):
    return salario_bruto - total_desc


main()