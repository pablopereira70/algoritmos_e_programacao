from utils import *

def main():
    menu = '''
--- APP N TUDO ---
[1] para iniciar
[0] para sair
------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo("-->", 0, 1)

        if comando == 1:
            texto = obter_texto_maximo("Digite a frase: ", 100)
            novo_texto = obter_novo_texto(texto)
            print(novo_texto)
        else:
            break 


def obter_novo_texto(texto):
    novo_texto = ''

    for ch in texto:
        if eh_vogal(ch):
            novo_texto += 3 * ch
        elif eh_cosoante(ch):
            novo_texto += 2 * ch
        else:
            novo_texto += ch

    return novo_texto


def eh_vogal(caractere):
    if ord(caractere) == 65 or ord(caractere) == 69 or ord(caractere) == 73 or ord(caractere) == 79 or ord(caractere) == 85 or ord(caractere) == 97 or ord(caractere) == 101 or ord(caractere) == 105 or ord(caractere) == 111 or ord(caractere) == 117:
        return True
    else:
        return False


def eh_cosoante(caractere):
    if ord(caractere) >= 66 and ord(caractere) <= 90 or ord(caractere) >= 98 and ord(caractere) <= 122:
        return True
    else:
        return False


main()