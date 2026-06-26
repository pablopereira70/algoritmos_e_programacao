from utils import *

selecoes = []
confederacoes = ["CONMEBOL", "UEFA", "CONCACAF", "CAF", "AFC", "OFC"]
grupos = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0}

def cadastrar_selecao():
    print("--- CADASTRO SELECAO ---") 
    if selecoes == 48:
        return print("[ERRO] O número de selecoes maximo foi atigindo")
    nome = obter_nome_selecao_valido()
    confederacao = obter_confederacao_valida()
    grupo = obter_grupo_valido(True)
    ranking_fifa = obter_ranking_fifa_valido()
    titulos = obter_inteiro_nao_negativo("Número de títulos: ")
    selecao_id = len(selecoes) + 1
    selecao = {"selecao_id" : selecao_id, "nome" : nome, "confederacao" : confederacao, "grupo" : grupo, "ranking_fifa": ranking_fifa, "titulos" : titulos}
    selecoes.append(selecao)
    print(f"[OK] A selecao {nome} foi cadastrada")

def listar_selecoes():
    print("--- LISTAR SELECOES ---")
    atributo = obter_atributo_selecao_valido()
    ordem = obter_inteiro_intervalo("Ordem? (1 - Crescente / 2 - Decrescente):", 1, 2)
    selecoes_ordenadas = sorted(selecoes, key=lambda selecao:selecao[atributo], reverse=(ordem == 2))

    print("+" + 4 * "-" + "+" + 12 * "-" + "+" + 7 * "-" + "+" + 14 * "-" + "+" + 9 * "-" + "+")
    print(f"|{"ID":^4}|{"Selecao":^12}|{"Grupo":^7}|{"Ranking FIFA":^14}|{"Titulos":^9}|")
    print("+" + 4 * "-" + "+" + 12 * "-" + "+" + 7 * "-" + "+" + 14 * "-" + "+" + 9 * "-" + "+")
    listar(selecoes_ordenadas, lambda selecao:f"|{str(selecao["selecao_id"]):^4}|{selecao["nome"]:^12}|{selecao["grupo"]:^7}|{str(selecao["ranking_fifa"]):^14}|{str(selecao["titulos"]):^9}|")
    print("+" + 4 * "-" + "+" + 12 * "-" + "+" + 7 * "-" + "+" + 14 * "-" + "+" + 9 * "-" + "+")


def buscar_selecao_por_nome():
    print(" --- BUSCAR SELECOES ---")
    nome = input("Nome ou parte do nome da seleção: ")
    nome = nome.strip().lower()
    selecoes_encontradas = []

    for selecao in selecoes:
        if nome in selecao["nome"].lower():
            selecoes_encontradas.append(selecao)

    if len(selecoes_encontradas) != 0:
        print("+" + 4 * "-" + "+" + 12 * "-" + "+" + 7 * "-" + "+" + 14 * "-" + "+" + 9 * "-" + "+")
        print(f"|{"ID":^4}|{"Selecao":^12}|{"Grupo":^7}|{"Ranking FIFA":^14}|{"Titulos":^9}|")
        print("+" + 4 * "-" + "+" + 12 * "-" + "+" + 7 * "-" + "+" + 14 * "-" + "+" + 9 * "-" + "+")
        listar(selecoes_encontradas, lambda selecao:f"|{str(selecao["selecao_id"]):^4}|{selecao["nome"]:^12}|{selecao["grupo"]:^7}|{str(selecao["ranking_fifa"]):^14}|{str(selecao["titulos"]):^9}|")
        print("+" + 4 * "-" + "+" + 12 * "-" + "+" + 7 * "-" + "+" + 14 * "-" + "+" + 9 * "-" + "+")
    else:
        print("[ERRO] Nenhuma seleção encontrada")


def filtrar_selecao_por_grupo_ou_confederacao():
    print("--- FILTRAR SELECOES ---")
    filtro = obter_filtro_selecao_valido()

    
    if filtro == "confederacao":
        nome_filtro = obter_confederacao_valida()
    else:
        nome_filtro = obter_grupo_valido(False)

    selecoes_filtradas = filtrar(selecoes, lambda selecao: selecao[filtro] == nome_filtro)

    if len(selecoes_filtradas) != 0:
        print("+" + 4 * "-" + "+" + 12 * "-" + "+" + 7 * "-" + "+" + 14 * "-" + "+" + 9 * "-" + "+")
        print(f"|{"ID":^4}|{"Selecao":^12}|{"Grupo":^7}|{"Ranking FIFA":^14}|{"Titulos":^9}|")
        print("+" + 4 * "-" + "+" + 12 * "-" + "+" + 7 * "-" + "+" + 14 * "-" + "+" + 9 * "-" + "+")
        listar(selecoes_filtradas, lambda selecao:f"|{str(selecao["selecao_id"]):^4}|{selecao["nome"]:^12}|{selecao["grupo"]:^7}|{str(selecao["ranking_fifa"]):^14}|{str(selecao["titulos"]):^9}|")
        print("+" + 4 * "-" + "+" + 12 * "-" + "+" + 7 * "-" + "+" + 14 * "-" + "+" + 9 * "-" + "+")
    else:
        print("[ERRO] Nenhuma seleção encontrada")


def obter_nome_selecao_valido():
    while True:
        nome = input("Nome da seleção: ")
        nome = nome.strip().title()

        if buscar(selecoes, lambda selecao:selecao["nome"], nome) == None:
            return nome
        
        print("[ERRO] Essa seleção já está cadastrada")
        

def obter_confederacao_valida():
    while True:
        print("--- CONFEDERACOES ---")
        listar(confederacoes, lambda confederacao:"> " + confederacao)
        print(10 * "=")
        confederacao = input("Nome da confederacao: ")
        confederacao = confederacao.strip().upper()

        if confederacao in confederacoes:
            return confederacao
        
        print("[ERRO] Essa confederação não existe")


def obter_grupo_valido(condicao):
    while True:
        print("--- GRUPOS ---")

        if condicao:
            listar(filtrar(grupos, lambda grupo:grupos[grupo] < 4), lambda grupo:"> Grupo " + grupo)
        else:
            listar(grupos, lambda grupo:"> Grupo" + grupo)

        print(20 * "-")

        grupo = input("Letra do grupo: ")
        grupo = grupo.strip().upper()

        if grupo in grupos:
            if condicao:
                if grupos[grupo] < 4:
                    grupos[grupo] += 1
                    return grupo
                else:
                    print("[ERRO] Esse grupo está cheio")
            return grupo
        else:
            print("[ERRO] Esse grupo não existe")


def obter_ranking_fifa_valido():
    while True:
        ranking_fifa = obter_inteiro_positivo("Número do ranking da fifa: ")

        if buscar(selecoes, lambda selecao:selecao["ranking_fifa"], ranking_fifa) == None:
            return ranking_fifa
        
        print("[ERRO] este número do ranking já está em uso")


def obter_atributo_selecao_valido():
     while True:
        atributos = ["nome", "ranking_fifa", "titulos"]
        atributo = input("Ordenar por qual atributo? (nome / ranking_fifa / titulos): ")
        atributo = atributo.strip().lower()

        if atributo in atributos:
            return atributo
        
        print("[ERRO] Esse atributo não existe")


def obter_filtro_selecao_valido():
    while True:
        filtros = ["grupo", "confederacao"]
        filtro = input("Filtrar por qual filtro? (grupo / confederacao): ")
        filtro = filtro.strip().lower()
        
        if filtro in filtros:
            return filtro
        
        print("[ERRO] Esse filtro não existe")