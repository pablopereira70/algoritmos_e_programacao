from q2_int_utils import *

def main():
    menu = '''
--- APP_SOMATÓRIO ---
[1] para iniciar
[0] para sair
---------------------'''

    while True:
        print(menu)
        comando = obter_inteiro_intervalo('-->', 0, 1)

        if comando == 1:
            inferior = obter_inteiro_positivo('Digite o limite inferior: ')
            superior = obter_inteiro_positivo('Digite o limite superior: ')

            for n in range(inferior, superior + 1):
                soma_divs = 0
                for i in range(1, n):
                    if n % i == 0:
                        soma_divs += i
                if n == soma_divs:
                    print(f'{n} é perfeito')
                else:
                    print(f'{n} não é perfeito')
        else:
            break


main()