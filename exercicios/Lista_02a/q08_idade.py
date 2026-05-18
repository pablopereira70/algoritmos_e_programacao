"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que recebe a data atual e a data de nascimento de uma pessoa, calcula a idade dessa pessoa, e exibe o resultado.
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

    idade = calcular_idade(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc)
    
    print(f'A idade dessa pessoa é de {idade} anos')


def calcular_idade(d_atual, m_atual, a_atual, d_nasc, m_nasc, a_nasc):
    idade = a_atual - a_nasc
    if (m_atual - m_nasc) < 0 or (m_atual - m_nasc) == 0 and d_atual < d_nasc:
        idade -= 1
    return idade


main()