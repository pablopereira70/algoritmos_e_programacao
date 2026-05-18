"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que calcula o valor a ser pago por um cliente em um açougue
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    carnes_disponiveis()
    tipo_carne = int(input())
    quant_carne = int(input('Digite a quantidade de carne(kg): '))
    formas_de_pagamento()
    tipo_pag = int(input())

    total_custo = obter_total_custo(tipo_carne, quant_carne)
    desc = obter_desc(tipo_pag, total_custo)
    valor_client = total_custo - desc
    texto_tipo_pag = obter_texto_tipo_pag(tipo_pag)
    texto_tipo_carne = obter_texto_tipo_carne(tipo_carne)

    print(f"""
              CUPOM FISCAL
Tipo de carne:           {texto_tipo_carne}
Quantidade de carne(kg): {quant_carne}
Preço total(R$):         {total_custo:.2f}
Tipo de pagamento:       {texto_tipo_pag}
Valor do desconto(R$):   {desc:.2f}
Valor a pagar(R$):       {valor_client:.2f}
""")
    

def carnes_disponiveis():
    print("""
     DIGITE
[1] para filé
[2] para alcatra
[3] para picanha""")
    

def formas_de_pagamento():
    print('''
  FORMAS DE PAGAMENTO
[1] cartão tabajara
[2] cartão de débito
[3] cartão de crédito
[4] pix
[5] dinheiro em espécie''')
    

def obter_total_custo(carne, kg):
    if carne == 1:
        if kg > 5:
            return kg * 5.8
        else:
            return kg * 4.9
    elif carne == 2:
        if kg > 5:
            return kg * 6.8
        else:
            return kg * 5.9
    else:
        if kg > 5:
            return kg * 7.8
        else:
            return kg * 6.9
        

def obter_desc(pag, total):
    if pag == 1:
        return total * 0.05
    else:
        return 0
    

def obter_texto_tipo_pag(pag):
    if pag == 1:
        return 'cartão tabajara'
    elif pag == 2:
        return 'cartão de débito'
    elif pag == 3:
        return 'cartão de crédito'
    elif pag == 4:
        return 'pix'
    else:
        return 'dinheiro em espécie'


def obter_texto_tipo_carne(carne):
    if carne == 1:
        return 'filé'
    elif carne == 2:
        return 'alcatra'
    else:
        return 'picanha'


main()