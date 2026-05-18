"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que recebe um número inteiro de até 3 dígitos e o exibe por extenso.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    num = int(input('Digite um número inteiro de até 3 dígitos: '))

    unidade = obter_unidade(num)
    dezena = obter_dezena(num)
    centena = obter_centena(num)
    texto_unidade = obter_texto_unidade(unidade)
    texto_dezena = obter_texto_dezena(dezena)
    texto_centena = obter_texto_centena(centena)
    separador_1 = obter_separador_1(centena, dezena, unidade)
    separador_2 = obter_separador_2(centena, dezena, unidade)
    

    print(f'{num} = {texto_centena}{separador_1}{texto_dezena}{separador_2}{texto_unidade}')


def obter_unidade(n):
    return n % 10


def obter_dezena(n):
    return (n % 100) // 10


def obter_centena(n):
    return n // 100


def obter_texto_unidade(U):
    if U == 0:
        return ''
    elif U == 1:
        texto = str(U) + ' unidade'
        return texto
    else:
        texto = str (U) + ' unidades'
        return texto


def obter_texto_dezena(D):
    if D == 0:
        return ''
    elif D == 1:
        texto = str(D) + ' dezena'
        return texto
    else:
        texto = str (D) + ' dezenas'
        return texto


def obter_texto_centena(C):
    if C == 0:
        return ''
    elif C == 1:
        texto = str(C) + ' centena'
        return texto
    else:
        texto = str (C) + ' centenas'
        return texto
    

def obter_separador_1(C, D, U):
    if C >= 1:
        if D >= 1 and U >= 1:
            return ", "
        elif D == 0 and U == 0:
            return ""
        else:
            return " e "
    else:
        return ""
    

def obter_separador_2(C, D, U):
    if D >= 1 and U >= 1:
        return " e "
    else:
        return ""
    

main()