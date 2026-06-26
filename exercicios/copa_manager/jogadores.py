from utils import *
from selecoes import *

jogadores = []
posicoes = ["Goleiro", "Zagueiro", "Meio", "Atacante"]


def cadastrar_jogador():
    print("--- CADASTRAR JOGADOR ---")

    if len(jogadores) == 48 * 26:
        return print("[ERRO] O número máximo de jogadores foi atingido")
    
    selecao_id = obter_selecao_id_valido()
    nome = obter_nome_jogador_valido()
    posicao = obter_posicao_valida()
    idade = obter_inteiro_minimo("Idade: ", 16)
    gols = obter_inteiro_nao_negativo("Gols ate agora: ")
    jogador_id = len(jogadores) + 100
    jogador = {"jogador_id" : jogador_id, "selecao_id" : selecao_id, "nome" : nome, "posicao" : posicao, "idade" : idade, "gols" : gols}
    jogadores.append(jogador)
    print(f"[OK] O jogador {nome} foi cadastrado e vinculado a selecao {selecoes[buscar(selecoes, lambda selecao:selecao["selecao_id"], selecao_id)]["nome"]}")


def listar_jogadores():
    print("--- LISTAR JOGADORES ---")
    atributo = obter_atributo_jogador_valido()
    ordem = obter_inteiro_intervalo("Ordem? (1 - Crescente / 2 - Decrescente):", 1, 2)
    jogadores_ordenadas = sorted(jogadores, key=lambda jogador:jogador[atributo], reverse=(ordem == 2))

    print("+" + 20 * "-" + "+" + 10 * "-" + "+" + 12 * "-" + "+" + 8 * "-" + "+")
    print(f"|{"Nome":^20}|{"Posicao":^10}|{"Selecao":^12}|{"Gols":^8}|")
    print("+" + 20 * "-" + "+" + 10 * "-" + "+" + 12 * "-" + "+" + 8 * "-" + "+")
    listar(jogadores_ordenadas, lambda jogador:f"|{str(jogador["nome"]):^20}|{jogador["posicao"]:^10}|{selecoes[buscar(selecoes, lambda selecao:selecao["selecao_id"], jogador["selecao_id"])]["nome"]:^12}|{str(jogador["gols"]) + " gols":^8}|")
    print("+" + 20 * "-" + "+" + 10 * "-" + "+" + 12 * "-" + "+" + 8 * "-" + "+")


def filtrar_jogadores():
    print("--- FILTRAR JOGADORES ---")
    filtro = obter_filtro_jogador_valido()

    if filtro == "posicao":
        posicao = obter_posicao_valida()
        jogadores_filtrados = filtrar(jogadores, lambda jogador:jogador["posicao"] == posicao)
    elif filtro == "faixa_de_idade":
        idade_min = obter_inteiro_positivo("Idade mínima: ")
        idade_max = obter_inteiro_minimo("Idade máxima: ", idade_min + 1)
        jogadores_filtrados = filtrar(jogadores, lambda jogador: jogador["idade"] >= idade_min and jogador["idade"] <= idade_max)
    else:
        nome = input("Nome ou fragmento do nome da selecao: ")
        jogadores_filtrados = filtrar(jogadores, lambda jogador:nome.lower() in selecoes[buscar(selecoes, lambda selecao:selecao["selecao_id"], jogador["selecao_id"])]["nome"].lower())

    if len(jogadores_filtrados) != 0:
        print("+" + 20 * "-" + "+" + 10 * "-" + "+" + 12 * "-" + "+" + 8 * "-" + "+")
        print(f"|{"Nome":^20}|{"Posicao":^10}|{"selecao":^12}|{"gols":^8}|")
        print("+" + 20 * "-" + "+" + 10 * "-" + "+" + 12 * "-" + "+" + 8 * "-" + "+")
        listar(jogadores_filtrados, lambda jogador:f"|{str(jogador["nome"]):^20}|{jogador["posicao"]:^10}|{selecoes[buscar(selecoes, lambda selecao:selecao["selecao_id"], jogador["selecao_id"])]["nome"]:^12}|{str(jogador["gols"]) + " gols":^8}|")
        print("+" + 20 * "-" + "+" + 10 * "-" + "+" + 12 * "-" + "+" + 8 * "-" + "+")
    else:
        print("[ERRO] Nenhum jogador encontrado")

def estatisticas_jogadores():
    print("--- ESTATISTICAS ---")
    nome = obter_selecao_valida()
    jogadores_selecao = filtrar(jogadores, lambda jogador:jogador["selecao_id"] == selecoes[buscar(selecoes, lambda selecao:selecao["nome"], nome)]["selecao_id"])
    total_de_gols = reduzir(jogadores_selecao, lambda jogador, soma_gols:jogador["gols"] + soma_gols, 0)
    media_de_idade = obter_media_de_idade(jogadores_selecao)
    atacantes_gols = obter_jogadores_mais_2_gols(jogadores_selecao)
    artilheiro = reduzir(jogadores, lambda jogador_atual, jogador:jogador_atual if jogador_atual["gols"] > jogador["gols"] else jogador, jogadores[0])
    artilheiro = artilheiro["nome"] + "(" + selecoes[buscar(selecoes, lambda selecao:selecao["selecao_id"], artilheiro["selecao_id"])]["nome"] + ") - " + str(artilheiro["gols"]) + " gols"

    print(f""" 
        - Total de jogadores: {len(jogadores_selecao)}
        - Total de gols do elenco: {total_de_gols} gols     (reduce) 
        - Media de idade: {media_de_idade:.1f} anos       (reduce / soma + len) 
        - Atacantes com +2 gols: {atacantes_gols}   (filter) 
        
        Artilheiro da Copa: {artilheiro}""")
    

def obter_selecao_id_valido():
    while True:
        print("--- SELECOES ---")
        listar(selecoes, lambda selecao:str(selecao["selecao_id"]) + " - " + selecao["nome"])
        print(20 * "-")
        selecao_id = obter_inteiro("Digite o ID da selecao: ")

        if buscar(selecoes, lambda selecao:selecao["selecao_id"], selecao_id) != None:
            if len(filtrar(jogadores, lambda jogador:jogador["selecao_id"] == selecao_id)) < 26:
                return selecao_id
            else:
                print("[ERRO] Essa seleção está cheia")

        print("[ERRO] Esse ID de seleção não existe")


def obter_nome_jogador_valido():
    while True:
        nome = input("Nome do jogador: ")
        nome = nome.strip().title()

        if buscar(jogadores, lambda jogador:jogador["nome"], nome) == None:
            return nome
        
        print("[ERRO] Esse jogador já está cadastrado")


def obter_posicao_valida():
    while True:
        posicao = input("Posicao (Goleiro/Zagueiro/Meio/Atacante): ")
        posicao = posicao.strip().title()

        if posicao in posicoes:
            return posicao
        else:
            print("[ERRO] Esse posição não existe")


def obter_atributo_jogador_valido():
    while True:
        atributos = ["nome", "posicao", "gols"]
        atributo = input("Ordenar por qual atributo? (nome / posicao / gols): ")
        atributo = atributo.strip().lower()

        if atributo in atributos:
            return atributo
        else:
            print("[ERRO] Esse atributo não existe")


def obter_filtro_jogador_valido():
    while True:
        filtros = ["posicao", "faixa_de_idade", "parte_do_nome_da_selecao"]
        filtro = input("Filtrar por qual filtro? (posicao / faixa_de_idade / parte_do_nome_da_selecao): ")
        filtro = filtro.strip().lower()
        
        if filtro in filtros:
            return filtro
        

def obter_selecao_valida():
    while True:
        print("--- SELECOES ---")
        listar(selecoes, lambda selecao:"> " + selecao["nome"])
        print(20 * "-")
        nome = input("Selecao: ")
        nome = nome.strip().title()

        if buscar(selecoes, lambda selecao:selecao["nome"], nome) != None:
            return nome
        else:
            print("[ERRO] Esse selecao não existe")


def obter_media_de_idade(colecao):
    if len(colecao) > 0:
        media_de_idade = reduzir(colecao, lambda jogador, soma_idade: jogador["idade"] + soma_idade, 0) / len(colecao)
    else:
        media_de_idade = 0

    return media_de_idade


def obter_jogadores_mais_2_gols(colecao):
    atacantes_gols = ""

    for jogador in filtrar(colecao, lambda jogador:jogador["gols"] > 2 and jogador["posicao"] == "Atacante"):
        atacantes_gols += jogador["nome"] + ", "

    return atacantes_gols[:len(atacantes_gols) - 2]