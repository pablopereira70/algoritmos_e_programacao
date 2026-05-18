from q3_float_utils import *
from q2_int_utils import *
from q4_text_utils import *

def main():
    menu = '''
--- APP_TALÃO ---
[1] para iniciar
[0] para sair
-----------------'''
    bandeiras = '''
--- BANDEIRAS ---
[1] verde
[2] amarela
[3] vermelha
[4] preta
-----------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo("--> ", 0, 1)

        if comando == 1:
            nome = obter_texto_minimo_e_maximo('Digite seu nome: ')
            consumo = obter_inteiro_positivo('Digite seu consumo mensal: ')
            print(bandeiras)
            bandeira = obter_inteiro_intervalo('Digite o número da bandeira: ', 1, 4)

            if consumo > 200:
                preco_consumo = consumo * (0.89 * 0.3)
            elif consumo > 30:
                preco_consumo = consumo * 0.89
            else:
                preco_consumo = 0

            if bandeira == 1:
                preco_bandeira = 0
            elif bandeira == 2:
                preco_bandeira = consumo // 100 * 2
            elif bandeira == 3:
                preco_bandeira = consumo // 100 * 5
            else:
                preco_bandeira = consumo // 100 * 10
            
            valor_total = preco_bandeira + preco_consumo
            icms = valor_total * 0.25
            pis_cofins = valor_total * 0.0375
            ilum_public = consumo // 80 * 0.4
            valor_pagar = valor_total + icms + pis_cofins + ilum_public

            print(f'''
****** TALÃO MENSAL XPTO ******** 
Consumidor: {nome}
Consumo (KWh): {consumo}  
Consumo (R$): R$ {preco_consumo:.2f} 
Bandeira Tarifária: R$ {preco_bandeira:.2f} 
Total sem Impostos: R$ {valor_total:.2f} 
ICMS: R$ {icms:.2f} 
PIS/COFINS: R$ {pis_cofins:.2f} 
Iluminação Pública: R$ {ilum_public:.2f} 
—-----------—-----------—-----------—----------- 
Total a Pagar: R$ {valor_pagar:.2f}''')
        else:
            break


main()