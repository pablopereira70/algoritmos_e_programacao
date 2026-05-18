from utils import *

def main():
    n = obter_inteiro('N: ')
    m = obter_inteiro_minimo('M: ', n + 1)

    numeros, soma = obter_numeros(n, m)

    if numeros == '':
        print('Nenhum número satisfaz a condição')
    else:
        print(f'''
    Números: {numeros}
    Soma:    {soma}''')
    

def obter_numeros(n, m):
    numeros = ''
    soma = 0
    
    for i in range(n, m + 1, +1):
        if i % 3 == 0:
            numeros += ' ' + str(i)
            soma += i

    return numeros, soma


main()