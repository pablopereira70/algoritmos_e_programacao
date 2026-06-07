"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    hora_inicio = int(input("Digite a hora inicial: "))
    min_inicio = int(input("Digite o minuto inicial: "))
    hora_final = int(input("Digite a hora final: "))
    min_final = int(input("Digite o minuto final: "))

    hora, min = obter_duracao(hora_inicio, min_inicio, hora_final, min_final)
    
    print(f'A duração do jogo corresponde: {hora} horas e {min} minutos.')


def obter_duracao(hora_in,min_in,hora_f,min_f):
    total_inicio = hora_in * 60 + min_in
    total_final = hora_f * 60 + min_f
    if total_final <= total_inicio:
        duracao = (total_final + 1440) - total_inicio
        hora = duracao // 60
        min = duracao % 60
    else:
        duracao = total_final - total_inicio
        hora = duracao // 60
        min = duracao % 60
        return hora, min


main()