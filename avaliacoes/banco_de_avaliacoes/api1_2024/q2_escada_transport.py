from utils import *

def main():
    menu = '''
--- APP_ATIVIDADE_FÍSICA ---
[1] para iniciar
[0] para sair
----------------------------'''

    while True:
        print(menu)
        comando = obter_inteiro_intervalo("-->", 0, 1)

        if comando == 1:
            sexo = obter_inteiro_intervalo('Digite seu sexo(M=1,F=2): ', 1, 2)
            peso_atual = obter_inteiro_positivo("Digite o seu peso: ")
            meta_kg = obter_inteiro_positivo("Digite quantos quilos quer perder: ")
            dias = obter_inteiro_intervalo("Digite quantos dias da semana você treina: ", 1, 7)
            tempo = obter_inteiro_positivo("Digite quanto tempo por dia(min): ")
            transport_porc = obter_inteiro_intervalo("Digite qual a porcentagem de tempo alocada ao transport: ", 0, 100)
            
            meta_cal = meta_kg * 7000
            tempo_transport = tempo * (transport_porc / 100)
            tempo_escada = tempo * ((100 - transport_porc) / 100)
            semanas = 0
            cal_transport = 0
            cal_escada = 0

            while True:
                semanas += 1
                if sexo == 1:
                    cal_transport += (dias * tempo_transport * 100 ) / 5
                    cal_escada += (dias * tempo_escada * 100) / 7
                else:
                    cal_transport += (dias * tempo_transport * 100 ) / 6
                    cal_escada += (dias * tempo_escada * 100) / 8

                if cal_transport + cal_escada >= meta_cal:
                    break

            print(f'''
----- INFORMAÇÕES -----
Semanas necessárias:  {semanas}
Minutos de transport: {tempo_transport}
Minutos de escada:   {tempo_escada}
----------------------- ''')
        else:
            break

main()