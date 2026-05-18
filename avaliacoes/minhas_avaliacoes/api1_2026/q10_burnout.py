from utils import *

def main():
    respondentes = 0
    soma_geral_burnout = 0
    maior_exaustao_emocional = -1
    menor_realizacao_pessoal = 7
    nome_maior_exaustao_emocional = ''
    nome_menor_realizacao_pessoal = ''

    while True:
        comando = exibir_menu()

        if comando == 1:
            respondentes += 1
            nome = obter_texto_minimo_e_maximo("Nome: ", 2)
            score_exaustao_emocional, score_despersonalizacao, score_realizacao_pessoal = obter_respostas()
            dimensao_exaustao_emocional, dimensao_despersonalizacao, dimensao_realizacao_pessoal = classificar_dimensao(score_exaustao_emocional, score_despersonalizacao, score_realizacao_pessoal)
            exibir_laudo(nome, score_exaustao_emocional, score_despersonalizacao, score_realizacao_pessoal, dimensao_exaustao_emocional, dimensao_despersonalizacao, dimensao_realizacao_pessoal)
            soma_geral_burnout += score_exaustao_emocional + score_despersonalizacao
            maior_exaustao_emocional, nome_maior_exaustao_emocional = atualizar_maior_exaustao_emocional(maior_exaustao_emocional, nome_maior_exaustao_emocional, score_exaustao_emocional, nome)
            menor_realizacao_pessoal, nome_menor_realizacao_pessoal = atualizar_menor_realizacao_pessoal(menor_realizacao_pessoal, nome_menor_realizacao_pessoal, score_realizacao_pessoal, nome)
        else:
            try:
                exibir_resumo(respondentes, soma_geral_burnout, nome_maior_exaustao_emocional, maior_exaustao_emocional, nome_menor_realizacao_pessoal, menor_realizacao_pessoal)
            except:
                print('Desculpe, não é possível gerar o resumo do estudo...')
            break

def obter_respostas():
    pergunta_1 = obter_inteiro_intervalo("Sinto-me emocionalmente esgotado(a) pelos meus estudos/trabalho: ", 0, 6)
    pergunta_2 = obter_inteiro_intervalo("Sinto-me esgotado(a) ao final de um dia de estudos/trabalho: ", 0, 6)
    pergunta_3 = obter_inteiro_intervalo("Acordar de manhã e ter que enfrentar mais um dia me causa cansaço: ", 0, 6)
    score_exaustao_emocional = calcular_score(pergunta_1, pergunta_2, pergunta_3)

    pergunta_4 = obter_inteiro_intervalo("Sinto que me tornei mais indiferente com as pessoas ao meu redor: ", 0, 6)
    pergunta_5 = obter_inteiro_intervalo("Tenho me preocupado menos com o impacto do meu trabalho/estudo nas pessoas: ", 0, 6)
    pergunta_6 = obter_inteiro_intervalo("Sinto que as pessoas ao meu redor me culpam por alguns dos seus problemas: ", 0, 6)
    score_despersonalizacao = calcular_score(pergunta_4, pergunta_5, pergunta_6)

    pergunta_7 = obter_inteiro_intervalo("Consigo lidar eficazmente com os problemas que surgem no meu dia a dia: ", 0, 6)
    pergunta_8 = obter_inteiro_intervalo("Sinto que estou tendo uma influência positiva na vida das pessoas: ", 0, 6)
    pergunta_9 = obter_inteiro_intervalo("Sinto-me estimulado(a) após trabalhar ou estudar com outras pessoas: ", 0, 6)
    score_realizacao_pessoal = calcular_score(pergunta_7, pergunta_8, pergunta_9)

    return score_exaustao_emocional, score_despersonalizacao, score_realizacao_pessoal


def calcular_score(resposta_1, resposta_2, resposta_3):
    return (resposta_1 + resposta_2 + resposta_3) / 3


def classificar_dimensao(score_exaustao, score_despersonal, score_realiza):
    if score_exaustao > 3.9:
        dimensao_exaustao = 'Alto'
    elif score_exaustao > 2:
        dimensao_exaustao = 'Moderado'
    else:
        dimensao_exaustao = 'Baixo'

    if score_despersonal > 3.9:
        dimensao_despersonal = 'Alto'
    elif score_despersonal > 2:
        dimensao_despersonal = 'Moderado'
    else:
        dimensao_despersonal = 'Baixo'
    
    if score_realiza > 3.9:
        dimensao_realiza = 'Alta'
    elif score_realiza > 2:
        dimensao_realiza = 'Moderada'
    else:
        dimensao_realiza = 'Baixa'

    return dimensao_exaustao, dimensao_despersonal, dimensao_realiza


def exibir_laudo(nome, score_exaustao, score_despersonal, score_realiza, dimensao_exaustao, dimensao_despersonal, dimensao_realiza):
    print(f'''
=========== LAUDO: {nome} ===========
Exaustão emocional : {score_exaustao:.2f} -> {dimensao_exaustao}
Despersonalização  :  {score_despersonal:.2f} -> {dimensao_despersonal}
Realização pessoal : {score_realiza:.2f} -> {dimensao_realiza}''')
    exibir_atencao(dimensao_exaustao, dimensao_despersonal, dimensao_realiza)
    

def exibir_menu():
    print("""
------------------ APP_BURNOUT ------------------
Bem-vindo você responderá a 9 perguntas divididas
em 3 dimensões para avaliar seu nível de esgotamento,
as perguntas seram respondidas numa escala de 0 a 6:
0 = nunca, 1 = raramente, 2 = às vezes, 3 = regularmente,
4 = frequentemente, 5 = quase sempre, 6 = sempre.
-------------------------------------------------
[1] para iniciar
[0] para sair""")
    return obter_inteiro_intervalo("--> ", 0, 1)


def atualizar_maior_exaustao_emocional(maior, nome_maior, possivel_maior, nome_possivel_maior):
    if possivel_maior > maior:
        return possivel_maior, nome_possivel_maior
    else:
        return maior, nome_maior


def atualizar_menor_realizacao_pessoal(menor, nome_menor, possivel_menor, nome_possivel_menor):
    if possivel_menor < menor:
        return possivel_menor, nome_possivel_menor
    else:
        return menor, nome_menor


def exibir_resumo(respondentes, somatorio, nome_maior_exaustao, maior_exaustao, nome_menor_realiza, menor_realiza):
    print(f'''
====== RESUMO DO ESTUDO ======
Respondentes        : {respondentes}
Maior exaustão      : {nome_maior_exaustao} ({maior_exaustao:.2f})
Menor realização    : {nome_menor_realiza} ({menor_realiza:.2f})
Média geral burnout : {somatorio / respondentes:.2f}''')


def exibir_atencao(dimensao_exaustao , dimensao_despersonal, dimensao_realiza):
    atencao = 0

    if dimensao_exaustao == 'Alto':
        atencao += 1

    if dimensao_despersonal == 'Alto':
        atencao += 1

    if dimensao_realiza == 'Baixa':
        atencao += 1

    if atencao > 0:
        print(f'''
Atenção: {atencao} dimensão(ões) em nível crítico.
Recomenda-se acompanhamento profissional.''')



main()