from q4_text_utils import *
from q2_int_utils import *

def main():
    menu = '''
--- APP_ANIMAL ---
[1] para iniciar
[0] para sair
------------------'''

    while True:
        print(menu)
        comando = obter_inteiro_intervalo("--> ", 0, 1)

        if comando == 1:
            quantidade = 0
            somatorio = 0
            animal = obter_texto_minimo_e_maximo("Digite o nome de um animal: ", 7)
            for i in animal:
                inteiro = obter_inteiro("Digite um número inteiro: ")
                eh_primo = verificar_eh_primo(inteiro)
                if eh_primo:
                    break
                somatorio += inteiro
                quantidade += 1
            if quantidade == 0:
                quantidade = 1
            print(f"somatório = {somatorio}")
            print(f"média = {somatorio/quantidade}")
        else:
            break


def verificar_eh_primo(n): 
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


main()