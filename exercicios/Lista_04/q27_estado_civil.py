"""
Disciplina: Algoritmos e Programação
Módulo: 04 - Estruturas de Repetição
Descrição: Programa para coletar informações sobre o estado civil e idade de entrevistados
Autor: Pablo Pereira
Data: Maio / 2026
"""

from utils import *

def main():
    menu = '''
--- APP_ESTADO_CIVIL ---
[1] para iniciar
[0] para sair
------------------------'''
    
    while True:
        exibir(menu)
        comando = obter_inteiro_intervalo(0, 1)
        limpar_tela()
        enter()
        limpar_tela()

        if comando == 1:
            masculino = 0
            feminino = 0
            idades_feminino = 0
            idades_masculino = 0
            solteiros = 0
            solteiras = 0
            quant_divorciadas = 0
            contador = 0

            while contador < 100:
                exibir_sexo()
                sexo = obter_inteiro_intervalo(1, 2)
                limpar_tela()
                idade = obter_inteiro_positivo('Digite a sua idade: ')
                limpar_tela()
                exibir_estado_civil()
                estado_civil = obter_inteiro_intervalo(1, 4)
                limpar_tela()
                contador += 1

                if sexo == 1:
                    masculino += 1
                    idades_masculino += idade

                    if estado_civil == 2:
                        solteiros += 1

                else:
                    feminino += 1
                    idades_feminino += idade

                    if estado_civil == 1:
                        solteiras += 1
                    elif estado_civil == 3 and idade > 30:
                        quant_divorciadas += 1
                
            exibir(f'''
------------------------ INFORMAÇÕES ------------------------
Média de idade  das mulheres:                        {idades_feminino / feminino:.1f}
Média de idade dos homens:                           {idades_masculino / masculino:.1f}
Percentual de homens solteiros:                      {solteiros / masculino * 100:.1f}% 
Percentual de mulheres solteiras:                    {solteiras / masculino * 100:.1f}%
Quantidade de mulheres divorciadas acima de 30 anos: {quant_divorciadas} 
-------------------------------------------------------------''')
            enter()
            limpar_tela()

        else:
            break


def exibir_sexo():
    exibir('''
--- OPÇÕES ---
[1] masculino
[2] feminino
--------------''')


def exibir_estado_civil():
    exibir('''
--- OPÇÕES ---
[1] solteiro
[2] casado
[3] divorciado
[4] viúvo''')


main()