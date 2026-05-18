from utils import *

def main():
    menu = '''
--- CADASTRO ---
[1] para iniciar
[0] para sair
----------------'''

    while True:
        print(menu)
        comando = obter_inteiro_intervalo('-->', 0, 1)

        if comando == 1:
            nome = obter_texto_minimo_e_maximo('Nome de usuário: ', 2, 20)
            senha = obter_senha()
            print(f'Olá {nome}, seja bem-vindo!')
        else:
            break


def obter_senha():
    while True:
        try:
            senha = obter_texto_minimo_e_maximo('Senha: ', 6, 6)
            eh_valida = verificar_eh_valida(senha)

            if eh_valida:
                return senha
            
            erro = 1 / 0
        except:
            print('senha inválida')


def verificar_eh_valida(s):
    if s[0] == 0:
        return False
    
    soma = 0
    for i in range(len(s)):
        try:
            if s[i] == s[i + 1]:
                return False
            soma += int(s[i])
        except:
            soma += int(s[i])
    
    if soma > 20:
        return True
    else:
        return False


main()