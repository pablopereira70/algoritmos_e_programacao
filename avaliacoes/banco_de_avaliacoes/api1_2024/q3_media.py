from utils import *

def main():
    menu = '''
--- APP_MÉDIA ---
[1] para iniciar
[0] para sair
-----------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo('-->', 0, 1)

        if comando == 1:
            somatorio = 0
            somatorio_fem = 0
            somatorio_masc = 0
            alunos = 0
            alunos_fem = 0
            alunos_masc = 0
            maior_nota = 0
            menor_nota = 10

            while True:
                sexo = obter_inteiro_intervalo('Digite o sexo(M=1,F=2 e FIM=3): ', 1, 3)

                if sexo == 3:
                    break

                nota = obter_real_intervalo('Digite a sua nota: ', 0, 10)

                if sexo == 2:
                    alunos += 1
                    somatorio += nota
                    alunos_fem += 1
                    somatorio_fem += nota
                else:
                    alunos += 1
                    somatorio += nota
                    alunos_masc += 1
                    somatorio_masc += nota

                maior_nota = obter_maior(nota, maior_nota)
                menor_nota = obter_menor(nota, menor_nota)

            media_turma = somatorio / alunos
            media_masc = somatorio_masc / alunos_masc
            media_fem = somatorio_fem / alunos_fem
            classif_turma = obter_classif(media_turma)
            classif_masc = obter_classif(media_masc)
            classif_fem = obter_classif(media_fem)

            print(f'''
------ PAINEL_DE_RENDIMENTO ------
Maior nota geral:        {maior_nota:.1f}
Menor nota geral:        {menor_nota:.1f}
Média da turma:          {media_turma:.1f}
Perfomance masculina:    {(somatorio_masc / (alunos_masc * 10)) * 100:.0f}%
Perfomance feminina:     {(somatorio_fem / (alunos_fem * 10)) * 100:.0f}%
Classificação da turma:  {classif_turma}
Classificação masculina: {classif_masc}
Classificação feminina:  {classif_fem}
----------------------------------''')
        else:
            break


def obter_maior(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


def obter_menor(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2


def obter_classif(media):
    if media > 8:
        return "Excelente"
    elif media > 7:
        return "Bom"
    elif media > 4:
        return "Regular"
    elif media > 2:
        return "Ruim"
    else:
        return "Pessímo"


main()