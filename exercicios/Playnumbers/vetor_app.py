import int_utils
import os_utils
import vetor_utils

def main():
    menu = """
>> APP_VETOR <<
1- Inicializar
2- Mostrar
3- Resetar
4- Tamanho
5- Maior e menor (reduce)
6- Somatório (reduce)
7- Média (reduce)
8- Positivos (filter)
9- Negativos (filter)
10- Atualizar (map)
11- Adicionar
12- Remover (valor)
13- Remover (posição) 
14- Substituir (posição)

0 - sair >>"""

    os_utils.limpa_tela()
    opcao = int_utils.obter_inteiro_intervalo(menu, 0, 15)

    while opcao != 0:
        
        if opcao == 1:
            vetor = vetor_utils.criar_vetor()
        try:
            if opcao == 2:
                print(vetor)
            elif opcao == 3:
                vetor = vetor_utils.resetar_vetor(len(vetor))
            elif opcao == 4:
                print("tamanho: ", len(vetor))
            elif opcao == 5:
                print("maior: ", vetor_utils.reduzir(vetor, lambda x,y: x if x > y else y, vetor[0]))
                print("menor: ", vetor_utils.reduzir(vetor, lambda x,y: x if x < y else y, vetor[0]))
            elif opcao == 6:
                print("somatorio: ", vetor_utils.reduzir(vetor, lambda x,y: x + y, 0))
            elif opcao == 7:
                print("media: ", vetor_utils.reduzir(vetor, lambda x,y: x + y, 0) / len(vetor))
            elif opcao == 8:
                print(vetor_utils.filtrar(vetor, lambda x: True if x > 0 else False))
            elif opcao == 9:
                print(vetor_utils.filtrar(vetor, lambda x: True if x < 0 else False))
            elif opcao == 10:
                vetor = vetor_utils.atualizar_valores(vetor)
            elif opcao == 11:
                numero = int_utils.obter_inteiro("Novo número: ")
                vetor.append(numero)
            elif opcao == 12:
                vetor = vetor_utils.remover_por_valor(vetor)
            elif opcao == 13:
                vetor_utils.remover_por_posicao(vetor)
            elif opcao == 14:
                vetor_utils.substituir_por_posicao(vetor)
        except:
            print("O vetor não foi criado")
                
        os_utils.enter()
        os_utils.limpa_tela()
        opcao = int_utils.obter_inteiro_intervalo(menu, 0, 15)

    try:
        vetor_utils.salvar_vetor(vetor)
    except:
        ...


main()