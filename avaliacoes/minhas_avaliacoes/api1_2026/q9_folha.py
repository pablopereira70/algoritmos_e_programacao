from utils import *

def main():
    total_folha_de_pag = 0
    maior_salario_liquido = 0
    menor_salario_liquido = 999999999
    nome_maior_salario_liquido = ''
    nome_menor_salario_liquido = ''
    menu = '''
--- APP_FOLHA_DE_PAGAMENTO ---
[1] para ler funcionário
[0] para sair
------------------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo('-->', 0, 1)
        if comando == 1:
            nome, salario_bruto, horas_extras = ler_funcionario()
            valor_hora_extra = calcular_hora_extra(salario_bruto, horas_extras)
            desconto_inss = salario_bruto / 100 * 11
            desconto_vale_refeicao = calcular_vale_refeicao(salario_bruto)
            salario_liquido = salario_bruto + valor_hora_extra - desconto_inss - desconto_vale_refeicao
            exibir_extrato_individual(nome, salario_bruto, horas_extras, valor_hora_extra, desconto_inss, desconto_vale_refeicao, salario_liquido)
            maior_salario_liquido, nome_maior_salario_liquido = atualizar_maior_salario_liquido(maior_salario_liquido, nome_maior_salario_liquido, salario_liquido, nome)
            menor_salario_liquido, nome_menor_salario_liquido = atualizar_menor_salario_liquido(menor_salario_liquido, nome_menor_salario_liquido, salario_liquido, nome)
            total_folha_de_pag += salario_liquido
        else:
            break
    exibir_extrato_completo(maior_salario_liquido, nome_maior_salario_liquido, menor_salario_liquido, nome_menor_salario_liquido, total_folha_de_pag)


def ler_funcionario():
    nome = obter_texto_minimo_e_maximo('Digite o nome do funcionário: ', 3)
    sal_bruto = obter_real_positivo('Digite o salário bruto: ')
    h_extra = obter_inteiro_positivo('Digite a quantidade de horas extras: ')

    return nome, sal_bruto, h_extra


def calcular_hora_extra(sal, h):
    return (sal / 220) * 1.5 * h


def calcular_vale_refeicao(sal):
    if sal > 2000:
        return 0
    else:
        return 150
    

def exibir_extrato_individual(nome, salario_bruto, horas_extras, valor_hora_extra, desconto_inss, desconto_vale_refeicao, salario_liquido):
    print(f'''
--- EXTRATO: {nome} ---
Salário Bruto: R$ {salario_bruto:.2f}
Horas Extras: R$ {valor_hora_extra:.2f} ({horas_extras}h)
INSS: R$ {desconto_inss:.2f}
Vale Refeição: R$ {desconto_vale_refeicao:.2f}
Salário Líquido: R$ {salario_liquido:.2f}
---''')
    

def atualizar_maior_salario_liquido(maior_salario_liquido, nome_maior_salario_liquido, salario_liquido, nome):
    if salario_liquido > maior_salario_liquido:
        return salario_liquido, nome
    else:
        return maior_salario_liquido, nome_maior_salario_liquido


def atualizar_menor_salario_liquido(menor_salario_liquido, nome_menor_salario_liquido, salario_liquido, nome):
    if salario_liquido < menor_salario_liquido:
        return salario_liquido, nome
    else:
        return menor_salario_liquido, nome_menor_salario_liquido
    

def exibir_extrato_completo(maior_salario_liquido, nome_maior_salario_liquido, menor_salario_liquido, nome_menor_salario_liquido, total_folha_de_pag):
    print(f'''
--- EXTRATO TOTAL ---
Maior salário líquido: R$ {maior_salario_liquido:.2f} ({nome_maior_salario_liquido})
Menor salário líquido: R$ {menor_salario_liquido:.2f} ({nome_menor_salario_liquido})
Total: R$ {total_folha_de_pag:.2f}
---''')


main()