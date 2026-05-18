"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa que simula uma eleição com 3 candidatos.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    n = int(input('Digite o número de eleitores: '))

    nulo = 0
    candidato_1 = 0
    candidato_2 = 0
    candidato_3 = 0
    branco = 0
    vencedor = None
    for i in range(n):
        print('''
VOTAÇÃO
[O] Nulo
[1] Candidato 1
[2] Candidato 2
[3] Candidato 3
[9] Branco''')
        voto = int(input())
        if voto == 0:
            nulo += 1
        elif voto == 1:
            candidato_1 += 1
        elif voto == 2:
            candidato_2 += 1
        elif voto == 3:
            candidato_3 += 1
        elif voto == 9:
            branco += 1
        else:
            print('valor inválido')
        
    if candidato_1 > candidato_2 and candidato_1 > candidato_3:
        vencedor = 'Candidato 1'
    elif candidato_2 > candidato_1 and  candidato_2 > candidato_3:
        vencedor = 'Candidato 2'
    else:
        vencedor = 'Candidato 3'
        
    print(f'Votos candidato 1: {candidato_1}')
    print(f'Votos candidato 2: {candidato_2}')
    print(f'Votos candidato 3: {candidato_3}')
    print(f'Votos nulos:       {nulo}')
    print(f'Votos brancos:     {branco}')
    print(f'Vencedor:          {vencedor}')


main()