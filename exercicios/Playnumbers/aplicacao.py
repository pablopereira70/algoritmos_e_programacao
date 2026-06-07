import int_utils
import os_utils

def main():
    menu = """
COLEÇÃO NÚMERICA
1- inicializar coleção
2- mostrar coleção
3- resetar coleção
4- tamanho coleção
5- mostrar maior e menor
6- somatorio da coleção
7- média da coleção
8- mostrar positivos
9- mostrar negativos

0- sair >>"""
    os_utils.limpa_tela()
    opcao = int_utils.obter_inteiro_intervalo(menu, 0, 8)
    # arvoré de operações
    while opcao != 0: # cria uma coleção
        if opcao == 1:
            colecao = criar_colecao()
        elif opcao == 2: # mostra a coleção
            print(colecao)
        elif opcao == 3: # reseta a coleção em um valor padrão
            colecao = resetar_colecao(len(colecao))
        elif opcao == 4:
            print(len(colecao))
        elif opcao == 5:
            num_menor, pos_menor = calcular_menor(colecao)
            num_maior, pos_maior = calcular_maior(colecao)
            print(f"Menor: {num_menor} Pos: {pos_menor}")
            print(f"Maior: {num_maior} Pos: {pos_maior}")
        elif opcao == 6:
            somatorio = calcular_somatorio(colecao)
            print(f"Somatório: {somatorio}")
        elif opcao == 7:
            media = calcular_media(colecao)
            print(f"Média: {media}")
        elif opcao == 8:
            mostrar_positivos(colecao)
        elif opcao == 9:
            mostrar_negativos(colecao)

        print(f"A opção {opcao} foi feita com sucesso!")
        enter()
        os_utils.limpa_tela()
        
        opcao = int_utils.obter_inteiro_intervalo(menu, 0, 8)
     

def enter():
    input('Pressione qualquer tecla....')


def criar_colecao():
    colecao = []
    menu_colecao = """
1- Gerar coleção
2- Inserir manual
3- Ler arquivo >>"""

    opcao = int_utils.obter_inteiro_intervalo(menu_colecao, 1, 3)

    if opcao == 1:
        valor_min = int_utils.obter_inteiro("Valor mínimo: ")
        valor_max = int_utils.obter_inteiro_minimo("Valor máximo: ", valor_min)
        colecao = [n for n in range(valor_min, valor_max + 1)]
    elif opcao == 2:
        elemento = input('Inserir elemento: ')

        while elemento != '':
            colecao.append(int(elemento))
            elemento = input('Inserir elemento: ')
    else:
        nome_arquivo = input('Nome do arquivo: ')
        arquivo = open(nome_arquivo)
        elemento = ''

        for line in arquivo:
            for ch in line:
                if ch == '\n':
                    continue
                elemento += ch
            colecao.append(int(elemento))
            elemento = ''
            
        arquivo.close()


    return colecao


def resetar_colecao(tam):
    val_padrao = int_utils.obter_inteiro('Valor padrão: ')
    colecao = [val_padrao for x in range(tam)]
    return colecao


def calcular_maior(colecao):
    num_maior = colecao[0]
    pos_maior = 0
    for i in range(1, len(colecao)):
        if num_maior < colecao[i]:
            num_maior = colecao [i]
            pos_maior = i
    return num_maior, pos_maior


def calcular_menor(colecao):
    num_menor = colecao[0]
    pos_menor = 0
    for i in range(1, len(colecao)):
        if num_menor > colecao[i]:
            num_menor = colecao [i]
            pos_menor = i
    return num_menor, pos_menor

def calcular_somatorio(colecao):
    somatorio = 0

    for val in colecao:
        somatorio += val

    return somatorio


def calcular_media(colecao):
    return calcular_somatorio(colecao) / len(colecao)


def mostrar_positivos(colecao):
    for item in colecao:
        if item > 0:
            print(item, end=' ')
    print()
    print(20 * '-')


def mostrar_negativos(colecao):
    for item in colecao:
        if item < 0:
            print(item, end=' ')
    print()
    print(20 * '-')
    

main()