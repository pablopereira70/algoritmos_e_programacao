from q2_int_utils import *

def main():
    menu = '''
--- APP_PRIMO ---
[1] para iniciar
[0] para sair
-----------------'''

    while True:
        print(menu)
        comando = obter_inteiro_intervalo('-->', 0, 1)

        if comando == 1:
            limite_inferior = obter_inteiro("Digite o número inteiro inicial: ")
            limite_superior = obter_inteiro_minimo("Digite um número inteiro final: ", limite_inferior + 1)

            for n in range(limite_inferior, limite_superior):
                divisores = 0
                if n < 2:
                    continue
                for i in range(2, int(n ** 0.5) + 1):
                    if n % i == 0:
                        divisores += 1
                        continue
                if divisores == 0:
                    print(n, end= ' - ')
            print('FIM')
                
        else:
            break


main()