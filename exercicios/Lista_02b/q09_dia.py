"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    num = int(input("Digite um número inteiro: "))

    dia_semana = obter_dia_semana(num)

    print(dia_semana)


def obter_dia_semana(n):
    if n == 1:
        return 'Domingo'
    elif n == 2:
        return 'Segunda'
    elif n == 3:
        return 'Terça'
    elif n == 4:
        return 'Quarta'
    elif n == 5:
        return 'Quinta'
    elif n == 6:
        return 'Sexta'
    elif n == 7:
        return 'Sabádo'
    else:
        return 'Valor inválido'
    

main()