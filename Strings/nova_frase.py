from utils import *

def main():
    menu = '''
--- APP NOVA FRASE ---
[1] para iniciar
[0] para sair
----------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo("-->", 0, 1)

        if comando == 1:
            texto = obter_texto('Digite o texto: ')
            novo_texto = my_replace(texto,' ')
            print(novo_texto)
        else:
            break

    print("xauuu")


def my_replace(texto, item_rm):
    novo_texto = ''

    for ch in texto:
        if ch != item_rm:
            novo_texto += ch

    return novo_texto


main()