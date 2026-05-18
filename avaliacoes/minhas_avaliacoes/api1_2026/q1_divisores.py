from utils import *

def main():
    n = obter_inteiro("N: ")

    divs, total = obter_divisores(n)

    print(f'''
Divisores: {divs}
Total:     {total}''')
    

def obter_divisores(n):
    divs = ''
    contador = 0

    if n > 0:
        for i in range(1, n + 1):
            if n % i == 0:
                divs += ' ' + str(i)
                contador += 1
    else:
        for i in range(n, 0, +1):
            if n % i == 0:
                divs += ' ' + str(i)
                contador += 1

        for i in range(1, (n - 1) * -1):
            if n % i == 0:
                divs += ' ' + str(i)
                contador += 1
        

    return divs, contador


main()