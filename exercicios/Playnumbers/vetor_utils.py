import int_utils
import os_utils
import random

def criar_vetor():
    sub_menu = """
>> CRIAR_VETOR <<
1- automático
2- manual
3- carregar >>"""  

    os_utils.limpa_tela()
    opcao = int_utils.obter_inteiro_intervalo(sub_menu, 1, 3)
    
    if opcao == 1:
        vetor = gerar_numeros()
    elif opcao == 2:
        vetor = inserir_numeros()
    else:
        vetor = carregar_numeros()

    return vetor

def gerar_numeros():
    os_utils.limpa_tela()
    valor_min = int_utils.obter_inteiro("Valor min: ")
    valor_max = int_utils.obter_inteiro_minimo("Valor max: ", valor_min)

    return [numero for numero in range(valor_min, valor_max + 1)]

def inserir_numeros():
    os_utils.limpa_tela()
    vetor = []
    tamanho = int_utils.obter_inteiro_positivo('Quantos números deseja inserir: ')
    contador = 0

    while contador < tamanho:
        contador += 1
        numero = int_utils.obter_inteiro("Número: ")
        vetor.append(numero)
    
    return vetor


def carregar_numeros():
    os_utils.limpa_tela()
    vetor = []

    while True:
        try:
            nome_arquivo = input("Nome do arquivo: ")

            for linha in open(nome_arquivo + ".txt"):
                vetor.append(int(linha.strip()))
            
            return vetor
        except:
            print("Algo deu errado!")


def resetar_vetor(tam):
    valor_padrao = int_utils.obter_inteiro("Valor padrão: ")

    return [valor_padrao for i in range(tam + 1)]


def reduzir(vetor, acumuladora, inicial):
    acumulador = inicial

    for numero in vetor:
        acumulador = acumuladora(numero, acumulador)

    return acumulador


def filtrar(vetor, criterio):
    filtrados = []

    for numero in vetor:
        if criterio(numero):
            filtrados.append(numero)

    return filtrados


def mapear(vetor, transformador):
    tranformados = []

    for numero in vetor:
        tranformados.append(transformador(numero))

    return tranformados


def atualizar_valores(vetor):
    sub_menu = """
>> ATUALIZAR_VETOR <<
1- Multiplicar
2- Elevar
3- Dividir
4- Ordenar
5- Embaralhar

0- Cancelar >>"""

    opcao = int_utils.obter_inteiro_intervalo(sub_menu, 0, 5)

    if opcao == 1:
        valor_padrao = int_utils.obter_inteiro("Valor padrão: ")
        novo_vetor = mapear(vetor, lambda x:x * valor_padrao)
    elif opcao == 2:
        valor_padrao = int_utils.obter_inteiro("Valor padrão: ")
        novo_vetor = mapear(vetor, lambda x: x ** valor_padrao)
    elif opcao == 3:
        valor_padrao = int_utils.obter_inteiro("Valor padrão: ")
        novo_vetor = mapear(vetor, lambda x: x / valor_padrao)
    elif opcao == 4:
        novo_vetor = ordenar_vetor(vetor)
    elif opcao == 5:
        novo_vetor = embaralhar_vetor(vetor)
    else:
        return

    return novo_vetor 


def ordenar_vetor(vetor):
    eh_reverso = int_utils.obter_inteiro_intervalo("Reverso: (sim = 1, não = 0)", 0, 1)
    
    if eh_reverso == 1:
        vetor_ordenado = sorted(vetor, reverse=True)
    else:
        vetor_ordenado = sorted(vetor)
    
    return vetor_ordenado


def embaralhar_vetor(vetor):
    return random.sample(vetor, len(vetor))


def remover_por_valor(vetor):
    valor = int_utils.obter_inteiro("Valor: ")

    for i in range(len(vetor)):
        if vetor[i] == valor:
            del vetor[i]


def remover_por_posicao(vetor):
    indice = int_utils.obter_inteiro_intervalo("Posição: ", 0, len(vetor) - 1)
    del vetor[indice]


def substituir_por_posicao(vetor):
    substituir_pos = int_utils.obter_inteiro_intervalo("Posição: ", 0, len(vetor) - 1)
    substituto = int_utils.obter_inteiro("Substituto: ")
    del vetor[substituir_pos]
    vetor.insert(substituir_pos, substituto)


def salvar_vetor(vetor):
    linhas = []

    for numero in vetor:
        linhas.append(str(numero) + "\n")

    arquivo = open("numbers.txt", mode= "w")
    arquivo.writelines(linhas)
    arquivo.close() 