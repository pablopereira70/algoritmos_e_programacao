from utils import *

def main():
    menu = '''
--- APP FORMATANDO HORAS ---
[1] para iniciar
[0] para sair
----------------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo("-->", 0, 1)

        if comando == 1:
            texto = obter_texto('Digite o texto: ')
            print(f"{texto[0]}{texto[1]} hora(s), {texto[3]}{texto[4]} minuto(s) e {texto[6]}{texto[7]} segundo(s)")
        else:
            break

    print("xauuu")


main()