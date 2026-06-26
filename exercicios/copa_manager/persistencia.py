from selecoes import *
from jogadores import *
from partidas import *

separador = ";"

def carregar_dados():
    print("Carregando dados...")

    for linha in open("selecoes.txt"):
        selecao = linha.strip().split(separador)
        selecao = {"selecao_id" : int(selecao[0]), "nome" : selecao[1], "confederacao" : selecao[2], "grupo" : selecao[3], "ranking_fifa": int(selecao[4]), "titulos" : int(selecao[5])}
        selecoes.append(selecao)
    
    print(f" - selecoes.txt ({len(selecoes)} registros) OK")
    
    for selecao in selecoes:
        for chave in grupos.keys():
            if selecao["grupo"] == chave:
                grupos[chave] += 1

    for linha in open("jogadores.txt"):
        jogador = linha.strip().split(separador)
        jogador = {"jogador_id" : int(jogador[0]), "selecao_id" : int(jogador[1]), "nome" : jogador[2], "posicao" : jogador[3], "idade" : int(jogador[4]), "gols" : int(jogador[5])}
        jogadores.append(jogador)

    print(f" - jogadores.txt ({len(jogadores)} registros) OK")
    
    for linha in open("partidas.txt"):
        partida = linha.strip().split(separador)
        partida = {"partida_id":int(partida[0]), "selecao_id_casa":int(partida[1]), "selecao_id_fora":int(partida[2]), "gols_casa":int(partida[3]), "gols_fora":int(partida[4]), "fase":partida[5]}
        partidas.append(partida)

    print(f" - partidas.txt ({len(partidas)} registros) OK")
    print("Pronto")

def salvar_dados():
    print("Salvando dados...")
    linhas = []

    for selecao in selecoes:
        linha = str(selecao["selecao_id"]) + separador + selecao["nome"] + separador + selecao["confederacao"] + separador + selecao["grupo"] + separador + str(selecao["ranking_fifa"]) + separador + str(selecao["titulos"]) + "\n"
        linhas.append(linha)

    arquivo = open("selecoes.txt", mode="w")
    arquivo.writelines(linhas)
    arquivo.close()

    print(f" - selecoes.txt ({len(linhas)} registros) OK")
    linhas = []
    
    for jogador in jogadores:
        linha = str(jogador["jogador_id"]) + separador + str(jogador["selecao_id"]) + separador + jogador["nome"] + separador + jogador["posicao"] + separador + str(jogador["idade"]) + separador + str(jogador["gols"])  + "\n"
        linhas.append(linha)

    arquivo = open("jogadores.txt", mode="w")
    arquivo.writelines(linhas)
    arquivo.close()
    
    print(f" - jogadores.txt ({len(linhas)} registros) OK")
    linhas = []

    for partida in partidas:
        linha = str(partida["partida_id"]) + separador + str(partida["selecao_id_casa"]) + separador + str(partida["selecao_id_fora"]) + separador + str(partida["gols_casa"]) + separador + str(partida["gols_fora"]) + separador + partida["fase"] + "\n"
        linhas.append(linha)

    arquivo = open("partidas.txt", mode="w")
    arquivo.writelines(linhas)
    arquivo.close()

    print(f" - partidas.txt ({len(linhas)} registros) OK")
    print("Ate a proxima!")