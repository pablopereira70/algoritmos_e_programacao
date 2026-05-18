from q2_int_utils import *

def main():
    menu = '''
--- APP_MDC ---
[1] para iniciar
[0] para sair
---------------'''

    while True:
        print(menu)
        comando = obter_inteiro_intervalo('-->', 0, 1)

        if comando == 1:
            num1 = obter_inteiro_positivo('Digite o primeiro número: ')
            num2 = obter_inteiro_positivo('Digite o segundo número: ')
            while True:
                resto = num1 % num2

                if resto == 0:
                    break

                num1 = num2
                num2 = resto
            print(f'mdc = {num2}')
        else:
            break


main()