"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    dia_atual = int(input('Digite o dia atual: '))
    mes_atual = int(input('Digite o mês atual: '))
    ano_atual = int(input('Digite o ano atual: '))
    dia_nasc = int(input('Digite o dia de nascimento: '))
    mes_nasc = int(input('Digite o mês de nascimento: '))
    ano_nasc = int(input('Digite o ano de nascimento: '))

    idade_ano,idade_mes,idade_dia = calcular_idade(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc)
    
    print(f'A idade dessa pessoa é de {idade_ano} anos, {idade_mes} meses e {idade_dia} dias')


def calcular_idade(dia_atual,mes_atual,ano_atual,dia_nasc,mes_nasc,ano_nasc):
    idade_ano = ano_atual - ano_nasc
    idade_mes = mes_atual - mes_nasc
    idade_dia = dia_atual - dia_nasc
    if idade_dia < 0:
        idade_mes -= 1
        idade_dia += 30
    if idade_mes < 0:
        idade_ano -= 1
        idade_mes += 12
    return idade_ano, idade_mes, idade_dia


main()