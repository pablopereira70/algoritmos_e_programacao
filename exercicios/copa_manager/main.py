from utils import *
from selecoes import *
from jogadores import *
from partidas import *
from persistencia import *

def main():
    limpar_tela()
    carregar_dados()
    enter()
    
    limpar_tela()
    print(obter_menu())
    opcao = obter_inteiro_intervalo("Escolha uma opção: ", 0, 12)

    while opcao != 0:
        if opcao == 1:
            cadastrar_selecao()
            enter()
        elif opcao == 2:
            listar_selecoes()
            enter()
        elif opcao == 3:
            buscar_selecao_por_nome()
            enter()
        elif opcao == 4:
            filtrar_selecao_por_grupo_ou_confederacao()
            enter()
        elif opcao == 5:
            cadastrar_jogador()
            enter()
        elif opcao == 6:
            listar_jogadores()
            enter()
        elif opcao == 7:
            filtrar_jogadores()
            enter()
        elif opcao == 8:
            estatisticas_jogadores()
            enter()
        elif opcao == 9:
            cadastrar_partida()
            enter()
        elif opcao == 10:
            listar_partidas()
            enter()
        elif opcao == 11:
            exibir_tabela_de_classificacao_por_grupo()
            enter()
        elif opcao == 12:
            salvar_dados()
            enter()

        limpar_tela()
        print(obter_menu())
        opcao = obter_inteiro_intervalo("Escolha uma opção: ", 0, 12)

    salvar_dados()


def obter_menu():
    return f"""
    ============================================================
    {'⚽ COPA MANAGER 2026 - FIFA ⚽':^60}
    ============================================================
    Status: {len(selecoes)} selecoes | {len(jogadores)} jogadores | {len(partidas)} partidas cadastradas
    ------------------------------------------------------------
    --- SELEÇÕES ---
    1. Cadastrar selecao
    2. Listar / ordenar selecoes
    3. Buscar selecao por nome
    4. Filtrar por grupo ou confederacao
  
    --- JOGADORES --- 
    5. Cadastrar jogador (vinculado a uma selecao) 
    6. Listar / ordenar jogadores 
    7. Filtrar jogadores 
    8. Artilheiros e estatisticas (media de idade, total de gols)

    --- PARTIDAS --- 
    9. Cadastrar partida 
   10. Listar partidas 
   11. Tabela de classificacao por grupo

    --- SISTEMA ---
   12. Salvar dados em arquivo
    0. Sair (salva automaticamente)
    ============================================================"""


main()