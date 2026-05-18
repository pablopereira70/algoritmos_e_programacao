"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para realizar uma pesquisa de opinião pública sobre as eleições
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
----- APP_OPINIÃO_PÚBLICA -----
[45] Serra
[13] Dilma
[23] Ciro Gomes
[99] Indeciso
[98] Outros
[0] Nulo/Branco
-------------------------------'''

    votos_serra, votos_dilma, votos_ciro, indecisos, votos_outros, votos_brancos, total_entrevistados, eh_2_turnos = ler_entrevistados(menu)

    exibir('------ RESULTADO DA PESQUISA ------')
    exibir(f'Votos em Serra:            {votos_serra:.1f}%')
    exibir(f'Votos em Dilma:            {votos_dilma:.1f}%')
    exibir(f'Votos em Ciro Gomes:       {votos_ciro:.1f}%')
    exibir(f'Entrevistados indecisos:   {indecisos:.1f}%')
    exibir(f'Votos em outros:           {votos_outros:.1f}%')
    exibir(f'Votos Nulos/Brancos:       {votos_brancos:.1f}%')
    exibir(f'Total de entrevistados:    {total_entrevistados}')
    exibir(f'Possibilidade de 2º turno: {eh_2_turnos}')


def ler_entrevistados(menu):
    entrevistados = 0
    votos_serra = 0
    votos_dilma = 0
    votos_ciro = 0
    indecisos = 0
    votos_outros = 0
    votos_brancos = 0

    while True:
        exibir(menu)
        voto_valido = obter_voto_valido('---> ')
        limpar_tela()
        enter()

        if voto_valido == -1:
            break
        elif voto_valido == 45:
            votos_serra += 1
        elif voto_valido == 13:
            votos_dilma += 1
        elif voto_valido == 23:
            votos_ciro += 1
        elif voto_valido == 99:
            indecisos += 1
        elif voto_valido == 98:
            votos_outros += 1
        else:
            votos_brancos += 1
        
        entrevistados += 1

    votos_serra = obter_porcentagem(votos_serra, entrevistados)
    votos_dilma = obter_porcentagem(votos_dilma, entrevistados)
    votos_ciro = obter_porcentagem(votos_ciro, entrevistados)
    indecisos = obter_porcentagem(indecisos, entrevistados)
    votos_outros = obter_porcentagem(votos_outros, entrevistados)
    votos_brancos = obter_porcentagem(votos_brancos, entrevistados)
    eh_2_turnos = verificar_se_eh_2_turnos(votos_serra, votos_dilma, votos_ciro)
    return votos_serra, votos_dilma, votos_ciro, indecisos, votos_outros, votos_brancos, entrevistados, eh_2_turnos 


def obter_voto_valido(conteudo):
    while True:

        try:
            voto = obter_inteiro(conteudo)

            if voto == -1:
                return voto
            elif voto == 45:
                return voto
            elif voto == 13:
                return voto
            elif voto == 23:
                return voto
            elif voto == 99:
                return voto
            elif voto == 98:
                return voto
            elif voto == 0:
                return voto
            
            erro = 1 / 0
        except:
            exibir("Voto inválido. Escolha um número listado(ex: 99)")


def verificar_se_eh_2_turnos(vs, vd, vc):
    if vs > 50.0 or vd > 50.0 or vc > 50.0:
        return 'Não'
    else:
        return 'Sim'

main()