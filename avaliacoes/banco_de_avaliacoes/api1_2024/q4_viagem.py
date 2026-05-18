from utils import *

def main():
    menu = '''
--- APP_MILHAS ---
[1] para iniciar
[0] para sair
------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo('-->', 0, 1)

        if comando == 1:
            origem = obter_texto("Digite sua origem: ")
            destino = obter_texto("Digite seu destino: ")
            valor_reais = obter_inteiro_positivo("Digite o valor do site(R$): ")
            valor_milhas = obter_inteiro_positivo("Digite o valor do site(milhas): ")

            milhas_padrao = 70 * (valor_milhas / 1000)
            milhas_baratas = 14.5 * (valor_milhas / 1000)

            melhor = obter_melhor(valor_reais, milhas_padrao, milhas_baratas)

            print(f'''
------ PROPOSTAS ------
Origem:        {origem}
Destino:       {destino}
--> 1º SITE
Valor(R$):     {valor_reais:.2f}
Valor(milhas): {valor_milhas}
--> 2º MILHAS PADRÃO
Valor(R$):     {milhas_padrao:.2f}
Porcentagem:   {milhas_padrao * 100 / valor_reais:.0f}%
--> 3º MILHAS BARATAS
Valor(R$):     {milhas_baratas:.2f}
Porcentagem:   {milhas_baratas * 100 / valor_reais:.0f}%
-----------------------
Melhor Proposta: {melhor}''')
        else:
            break


def obter_melhor(p1, p2, p3):
    menor = p1
    melhor = 'Site'

    if p2 < menor:
        menor = p2
        melhor = 'Milhas padrão'

    if p3 < menor:
        melhor = 'Milhas baratas'

    return melhor


main()