"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    pergunta_1 = input('Telefonou para a vítima ?(sim/não)')
    pergunta_2 = input('Esteve no local do crime?(sim/não)')
    pergunta_3 = input('Mora perto da vítima?(sim/não)')
    pergunta_4 = input('Devia para a vítima?(sim/não)')
    pergunta_5 = input('Já trabalhou com a vítima ?(sim/não)')

    quant_sim = obter_quant_sim(pergunta_1, pergunta_2, pergunta_3, pergunta_4, pergunta_5)
    classificacao = obter_classificacao(quant_sim)

    print(classificacao)


def obter_quant_sim(p1, p2, p3, p4, p5):
    quant = 0

    if p1 == "sim":
        quant += 1
    
    if p2 == "sim":
        quant += 1
    
    if p3 == "sim":
        quant += 1
    
    if p4 == "sim":
        quant += 1 

    if p5 == "sim":
        quant += 1

    return quant


def obter_classificacao(quant):
    if quant == 5:
        return "Assassino"
    elif quant > 2:
        return "Cúmplice"
    elif quant == 2:
        return "Suspeita"
    else:
        return "Inocente"