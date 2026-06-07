"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    ano_data1 = int(input('Digite o ano da primeira data: '))
    mes_data1 = int(input('Digite o mês da primeira data: '))
    dia_data1 = int(input('Digite o dia da primeira data: '))
    ano_data2 = int(input('Digite o ano da segunda data: '))
    mes_data2 = int(input('Digite o mês da segunda data: '))
    dia_data2 = int(input('Digite o dia da segunda data: '))

    data_recente = obter_data_recente(ano_data1,mes_data1,dia_data1,ano_data2,mes_data2,dia_data2)
    
    if data_recente == 1:
        print(f'a data mais recente: {dia_data1}/{mes_data1}/{ano_data1}')
    else:
        print(f'a data mais recente: {dia_data2}/{mes_data2}/{ano_data2}')


def obter_data_recente(ano1,mes1,dia1,ano2,mes2,dia2):
    if ano1 > ano2:
        return 1
    elif ano2 > ano1:
        return 2
    elif mes1 > mes2:
        return 1
    elif mes2 > mes1:
        return 2
    elif dia1 > dia2:
        return 1
    else:
        return 2
    

main()