"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que recebe dois números inteiros e realiza operações com base no resto da divisão.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    var_1 = int(input('Digite um número inteiro qualquer: '))
    var_2 = int(input('Digite um número inteiro qualquer: '))
    painel_de_selecao()
    qual_operacao = int(input())

    resultado = executar_operacao(var_1,var_2,qual_operacao)
    
    print(resultado)


def painel_de_selecao():
    print("""
SELECIONE A OPERAÇÃO:
[1] Adição 
[2] Subtração
[3] Multiplicação
[4] Divisão
""")
    

def executar_operacao(n1,n2,op):
    if op == 1:
        return n1 + n2
    elif op == 2:
        return n1 - n2
    elif op == 3:
        return n1 * n2
    elif op == 4 and n2 != 0:
        return n1 / n2
    else:
        return 'NÚMERO INVÁLIDO'
    

main()