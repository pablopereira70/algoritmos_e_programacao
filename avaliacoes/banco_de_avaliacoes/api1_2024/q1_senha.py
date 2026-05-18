from utils import *
import random

def main():
    menu = '''
--- APP_GERADOR_DE_SENHAS ---
[1] para iniciar
[0] para sair
-----------------------------'''
    
    while True:
        print(menu)
        comando = obter_inteiro_intervalo("--> ", 0, 1)

        if comando == 1:
            tamanho = obter_inteiro_positivo("Digite o tamanho da senha: ")
            while True:
                senha = gerar_senha(tamanho)
                satisfeito = verificar_satisfeito(senha)

                if satisfeito:
                    break
        else:
            break


def gerar_senha(tam):
    senha = ''
    digito = random.randint(1, 9)
    senha += str(digito)
    digito_anterior = digito
    contador = tam - 1

    while contador > 0:
        digito = random.randint(1, 9)

        if digito != digito_anterior and digito != digito_anterior + 1 and digito != digito_anterior - 1:
            digito_anterior = digito
            senha += str(digito)
            contador -= 1

    return senha


def verificar_satisfeito(senha):
    print(f'''
Senha: {senha}
Você está satisfeito?
[1] para sim
[2] para não''')
    num = obter_inteiro_intervalo('-->', 1, 2)
    if num == 1:
        return True
    else:
        return False


main()