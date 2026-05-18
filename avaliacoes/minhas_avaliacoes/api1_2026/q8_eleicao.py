from utils import *

def main():
    menu = '''
--- URNA ELETRÔNICA ---
[1] para inserir candidatos
[2] para modo votação
[0] para sair
-----------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo('--->', 0, 2)

        if comando == 1:
            nome_c1, nome_c2, nome_c3, nome_c4 = inserir_candidatos()
        elif comando == 2:
            try:
                modo_votacao(nome_c1, nome_c2, nome_c3, nome_c4)
            except:
                print('Nenhum candidato foi inserido!')
        else:
            break


def inserir_candidatos():
    nome_c1 = obter_texto_minimo_e_maximo('Digite o nome do candidato: ', 4)
    nome_c2 = obter_texto_minimo_e_maximo('Digite o nome do candidato: ', 4)
    nome_c3 = obter_texto_minimo_e_maximo('Digite o nome do candidato: ', 4)
    nome_c4 = obter_texto_minimo_e_maximo('Digite o nome do candidato: ', 4)

    return nome_c1, nome_c2, nome_c3, nome_c4


def modo_votacao(candidato_1, candidato_2, candidato_3, candidato_4):
    voto_c1, voto_c2, voto_c3, voto_c4, voto_branco, voto_nulo = 0, 0, 0, 0, 0, 0
    menu_votacao = '''
--- OPÇÕES ---
[1] para votar
[2] para resultado parcial
[0] para encerrar
--------------'''
    while True:
        print(menu_votacao)
        comando = obter_inteiro_intervalo('-->', 0, 2)

        if comando == 1:
            voto_c1, voto_c2, voto_c3, voto_c4, voto_branco, voto_nulo, votos_total = votar(voto_c1, voto_c2, voto_c3, voto_c4, voto_branco, voto_nulo, candidato_1, candidato_2, candidato_3, candidato_4)
        elif comando == 2:
            try:
                exibir_resultado_parcial(voto_c1, voto_c2, voto_c3, voto_c4, voto_branco, voto_nulo, votos_total, candidato_1, candidato_2, candidato_3, candidato_4)
            except:
                print('Não há votos computados!')
        else:
            break
    try:
        exibir_resultado(voto_c1, voto_c2, voto_c3, voto_c4, voto_branco, voto_nulo, votos_total, candidato_1, candidato_2, candidato_3, candidato_4)
    except:
        print('Não há votos computados!')


def votar(voto_c1, voto_c2, voto_c3, voto_c4, voto_branco, voto_nulo, candidato_1, candidato_2, candidato_3, candidato_4):
    print(f'''
1 - {candidato_1}
2 - {candidato_2}
3 - {candidato_3}
4 - {candidato_4}
5 - voto nulo
0 - voto branco
---''')
    voto = obter_inteiro_intervalo('Digite seu voto: ', 0, 5)
    total = voto_c1 + voto_c2 + voto_c3 + voto_c4 + voto_branco + voto_nulo + 1

    if voto == 1:
        return voto_c1 + 1, voto_c2, voto_c3, voto_c4, voto_branco, voto_nulo, total
    elif voto == 2:
        return voto_c1, voto_c2 + 1, voto_c3, voto_c4, voto_branco, voto_nulo, total
    elif voto == 3:
        return voto_c1, voto_c2, voto_c3 + 1, voto_c4, voto_branco, voto_nulo, total
    elif voto == 4:
        return voto_c1, voto_c2, voto_c3, voto_c4 + 1, voto_branco, voto_nulo, total
    elif voto == 5:
        return voto_c1, voto_c2, voto_c3, voto_c4, voto_branco, voto_nulo + 1, total
    else:
        return voto_c1, voto_c2, voto_c3, voto_c4, voto_branco + 1, voto_nulo, total


def exibir_resultado_parcial(voto_c1, voto_c2, voto_c3, voto_c4, voto_branco, voto_nulo,votos_total, candidato_1, candidato_2, candidato_3, candidato_4):
    print(f'''
--- PARCIAL ---
{votos_total} votos

{candidato_1} --> {voto_c1}
{candidato_2} --> {voto_c2}
{candidato_3} --> {voto_c3}
{candidato_4} --> {voto_c4}
votos brancos --> {voto_branco}
votos nulos --> {voto_nulo}
---------------''')


def exibir_resultado(voto_c1, voto_c2, voto_c3, voto_c4, voto_branco, voto_nulo,votos_total, candidato_1, candidato_2, candidato_3, candidato_4):
    vencedor = obter_vencedor(voto_c1, voto_c2, voto_c3, voto_c4, candidato_1, candidato_2, candidato_3, candidato_4)
    print(f'''
--- RESULTADO ---
{candidato_1} --> {voto_c1} ({voto_c1 / votos_total * 100:.1f}%)
{candidato_2} --> {voto_c2} ({voto_c2 / votos_total * 100:.1f}%)
{candidato_3} --> {voto_c3} ({voto_c3 / votos_total * 100:.1f}%)
{candidato_4} --> {voto_c4} ({voto_c4 / votos_total * 100:.1f}%)
votos brancos --> {voto_branco} ({voto_branco / votos_total * 100:.1f}%)
votos nulos --> {voto_nulo} ({voto_nulo / votos_total * 100:.1f}%)
vencedor ---> {vencedor}
-----------------''')
    

def obter_vencedor(voto_c1, voto_c2, voto_c3, voto_c4, candidato_1, candidato_2, candidato_3, candidato_4):
    votos_validos = voto_c1 + voto_c2 + voto_c3 + voto_c4
    maior_voto = voto_c1
    vencedor = candidato_1
    empate = False

    if voto_c2 > maior_voto:
        maior_voto = voto_c2
        vencedor = candidato_2
        empate = False
    elif voto_c2 == maior_voto:
        empate = True

    if voto_c3 > maior_voto:
        maior_voto = voto_c3
        vencedor = candidato_3
        empate = False
    elif voto_c3 == maior_voto:
        empate = True

    if voto_c4 > maior_voto:
        maior_voto = voto_c4
        vencedor = candidato_4
        empate = False
    elif voto_c4 == maior_voto:
        empate = True

    if maior_voto == 0:
        return "Sem votos nos candidatos"
    
    if empate:
        return "Segundo Turno (Empate)"
    
    if maior_voto <= (votos_validos / 2):
        return "Segundo Turno (O líder não atingiu mais da metade dos votos válidos)"
    
    return vencedor


main()