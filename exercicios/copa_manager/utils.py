import platform
import os

def obter_inteiro(conteudo):
    while True:

        try:
            inteiro = int(input(conteudo))
            return inteiro
        except:
            print("[ERRO] Isso não é um número inteiro")


def obter_inteiro_positivo(conteudo):
    while True:

        try:
            inteiro = obter_inteiro(conteudo)

            if inteiro > 0:
                return inteiro
            
            erro = 1 / 0
        except:
            print("[ERRO] Isso não é um número inteiro positivo")


def obter_inteiro_minimo(conteudo, limite_inferior):
    while True:

        try:
            inteiro = obter_inteiro(conteudo)

            if inteiro >= limite_inferior:
                return inteiro
            
            erro = 1 / 0
        except:
            print(f"[ERRO] Esse número é menor que {limite_inferior}")


def obter_inteiro_maximo(conteudo, limite_superior):
    while True:

        try:
            inteiro = obter_inteiro(conteudo)

            if inteiro <= limite_superior:
                return inteiro
            
            erro = 1 / 0
        except:
            print(f"[ERRO] Esse número é maior que {limite_superior}")


def obter_inteiro_intervalo(conteudo, limite_inferior, limite_superior):
    while True:
        try:
            inteiro = obter_inteiro(conteudo)

            if inteiro >= limite_inferior and inteiro <= limite_superior:
                return inteiro
            
            erro = 1 / 0
        except:
            print(f"[ERRO] Esse número não está na faixa {limite_inferior} -- {limite_superior}")


def obter_inteiro_nao_negativo(conteudo):
    while True:

        try:
            inteiro = obter_inteiro(conteudo)

            if inteiro >= 0:
                return inteiro
            
            erro = 1 / 0
        except:
            print("[ERRO] Isso não é um número inteiro não negativo")


def filtrar(colecao, criterio):
    filtrados = []

    for item in colecao:
        if criterio(item):
            filtrados.append(item)

    return filtrados


def reduzir(colecao, operacao, inicial):
    acumulador = inicial

    for item in colecao:
        acumulador = operacao(item, acumulador)

    return acumulador


def mapear(colecao, funcao):
    tranformados = []

    for item in colecao:
        tranformados.append(funcao(item))

    return tranformados


def listar(colecao, formatador):
    for item in colecao:
        print(formatador(item))


def buscar(colecao, formatador, item):
    for indice in range(len(colecao)):
        if formatador(colecao[indice]) == item:
            return indice
        
    return None


def limpar_tela():
    sistema = platform.system()

    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def enter():
    input("Pressione ENTER para voltar ao menu...")