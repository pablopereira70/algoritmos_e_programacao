from utils import *
from selecoes import *

partidas = []
fases = ["Grupos", "Round Of 32", "Oitavas", "Quartas", "Semifinais", "Final"]

def cadastrar_partida():
    if len(selecoes) == 0:
        return print("[ERRO] não há selecoes cadastradas")
    
    selecao_id_casa = obter_selecao_id_casa_valido()
    selecao_id_fora = obter_selecao_id_fora_valido(selecao_id_casa)
    gols_casa = obter_inteiro_nao_negativo("Digite o numero de gols do mandante: ")
    gols_fora = obter_inteiro_nao_negativo("Digite o numero de gols do visitante: ")
    fase = obter_fase_valida()
    partida_id = len(partidas) + 5000
    partida = {"partida_id":partida_id, "selecao_id_casa":selecao_id_casa, "selecao_id_fora":selecao_id_fora, "gols_casa":gols_casa, "gols_fora":gols_fora, "fase":fase}
    partidas.append(partida)


def listar_partidas():
    if len(partidas) != 0:
        listar(partidas, lambda partida:selecoes[buscar(selecoes, lambda selecao:selecao["selecao_id"], partida["selecao_id_casa"])]["nome"] + " " + str(partida["gols_casa"]) + " x " + str(partida["gols_fora"]) + " " + selecoes[buscar(selecoes, lambda selecao:selecao["selecao_id"], partida["selecao_id_fora"])]["nome"] + " (" + partida["fase"] + ")")
    else:
        print("Nenhuma partida cadastrada")


def exibir_tabela_de_classificacao_por_grupo():
    grupo = obter_grupo_valido(False)
    selecoes_grupo = filtrar(selecoes, lambda selecao: selecao["grupo"] == grupo)
    partidas_grupo = filtrar(partidas, lambda partida:partida["fase"] == "Grupos" and buscar(selecoes_grupo, lambda selecao: selecao["selecao_id"], partida["selecao_id_casa"]) is not None and buscar(selecoes_grupo, lambda selecao: selecao["selecao_id"], partida["selecao_id_fora"]) is not None)
    selecoes_estatist = obter_selecoes_estatist(selecoes_grupo, partidas_grupo)
    selecoes_estatist = sorted(selecoes_estatist, key=lambda selecao: (selecao["P"], selecao["SG"], selecao["GP"]), reverse=True)

    print(f"--- CLASSIFICACAO - GRUPO {grupo} ---")
    print(f"{"Pos":<5}{"Selecao":<13}{"P":<4}{"V":<3}{"E":<3}{"D":<4}{"GP":<4}{"GC":<4}{"SG":<4}")
    listar(selecoes_estatist, lambda selecao:f"{str(buscar(selecoes_estatist, lambda s:s["nome"],selecao["nome"]) + 1) + "o":<5}{selecao["nome"]:<13}{selecao["P"]:<4}{selecao["V"]:<3}{selecao["E"]:<3}{selecao["D"]:<4}{selecao["GP"]:<4}{selecao["GC"]:<4}{selecao["SG"]:<+4}")
    print("(P=Pontos, V/E/D=Vitorias/Empates/Derrotas, GP/GC=Gols Pro/Contra, SG=Saldo)")


def obter_selecao_id_casa_valido():
    while True:
        print("--- SELECOES ---")
        listar(selecoes, lambda selecao:str(selecao["selecao_id"]) + " - " + selecao["nome"])
        print(20 * "-")
        selecao_id_casa = obter_inteiro("Digite o ID da selecao mandante: ")
        if buscar(selecoes, lambda selecao:selecao["selecao_id"], selecao_id_casa) != None:
            return selecao_id_casa
        else:
            print("Esse selecao ID não existe")


def obter_selecao_id_fora_valido(id_casa):
    while True:
        print("--- SELECOES ---")
        listar(selecoes, lambda selecao:str(selecao["selecao_id"]) + " - " + selecao["nome"])
        print(20 * "-")
        selecao_id_fora = obter_inteiro("Digite o ID da selecao visitante: ")
        if buscar(selecoes, lambda selecao:selecao["selecao_id"], selecao_id_fora) != None:
            if selecao_id_fora != id_casa:
                return selecao_id_fora
            else:
                print("Essa selecao ID é o mesmo")
        
        print("Esse selecao ID não existe")


def obter_fase_valida():
    while True:
        print("--- FASES ---")
        listar(fases, lambda fase:"> " + fase)
        print(20 * "-")
        fase = input("Digite a fase: ")
        fase = fase.strip().title()
        if fase in fases:
            return fase
        else:
            print("Essa fase não existe")


def obter_selecoes_estatist(s_grupo, p_grupo):
    selecoes_estatist = []

    for selecao in s_grupo:
        selecao_estatist = {"nome":selecao["nome"], "P":0, "V":0, "E":0, "D":0, "GP":0, "GC":0, "SG":0}
        for partida in p_grupo:
            if partida["selecao_id_casa"] == selecao["selecao_id"]:
                if partida["gols_casa"] > partida["gols_fora"]:
                    selecao_estatist["P"] += 3
                    selecao_estatist["V"] += 1
                elif partida["gols_casa"] == partida["gols_fora"]:
                    selecao_estatist["P"] += 1
                    selecao_estatist["E"] += 1
                else:
                    selecao_estatist["D"] += 1
                selecao_estatist["GP"] += partida["gols_casa"]
                selecao_estatist["GC"] += partida["gols_fora"]
            elif partida["selecao_id_fora"] == selecao["selecao_id"]:
                if partida["gols_fora"] > partida["gols_casa"]:
                    selecao_estatist["P"] += 3
                    selecao_estatist["V"] += 1
                elif partida["gols_fora"] == partida["gols_casa"]:
                    selecao_estatist["P"] += 1
                    selecao_estatist["E"] += 1
                else:
                    selecao_estatist["D"] += 1
                selecao_estatist["GP"] += partida["gols_fora"]
                selecao_estatist["GC"] += partida["gols_casa"]
        selecao_estatist["SG"] = selecao_estatist["GP"] - selecao_estatist["GC"]
        selecoes_estatist.append(selecao_estatist)

    return selecoes_estatist