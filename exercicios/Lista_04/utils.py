import platform
import os

def obter_inteiro(conteudo):
    while True:

        try:
            inteiro = int(input(conteudo))
            return inteiro
        except:
            print("Valor inválido. Isso não é um número inteiro(ex: ...,-2,-1,0,1,2,...)")


def obter_inteiro_nao_nulo(conteudo):
    while True:
        
        try:
            inteiro = int(input(conteudo))

            if inteiro != 0:
                return inteiro
            
            erro = 1 / 0
        except:
            print("Valor inválido. Isso  não é um número inteiro não nulo(ex: ...,-2,-1,1,2...)")


def transformar_positivo(n):
    if n < 0:
        return n * -1
    
    return n


def obter_texto(conteudo):
    texto = input(conteudo)
    return texto


def obter_real(conteudo):
    while True:

        try:
            real = float(input(conteudo))
            return real
        except:
            print("Valor inválido. Isso não é um número real(ex: ...,-0.9,0.0,0.1,...)")


def exibir(conteudo):
    try:
        print(conteudo)
    except:
        print('Desculpe. Ocorreu algum erro...')


def limpar_tela():
    sistema = platform.system()

    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def enter():
    obter_texto("Pressione enter... ")


def obter_real_positivo(conteudo):
    while True:

        try:
            real = float(input(conteudo))
            if real >= 0:
                return real
            erro = 1 / 0
        except:
            print("Valor inválido. Isso não é um número real positivo(ex: 0.0,0.1,0.2...)")


def obter_porcentagem(parcial, total):
    return (parcial * 100) / total


def obter_inteiro_intervalo(limite_inferior, limite_superior):
    while True:
        try:
            inteiro = obter_inteiro(f"Digite um número inteiro entre {limite_inferior} a {limite_superior}: ")

            if inteiro >= limite_inferior and inteiro <= limite_superior:
                return inteiro
            
            erro = 1 / 0
        except:
            exibir(f"Valor inválido. Isso não é um número inteiro do intervalo [{limite_inferior}, {limite_superior}]")


def obter_inteiro_positivo(conteudo):
    while True:

        try:
            inteiro = obter_inteiro(conteudo)

            if inteiro >= 0:
                return inteiro
            
            erro = 1 / 0
        except:
            exibir('Valor inválido. Isso não é um número inteiro positivo (ex: 0,1,2,3,...)')