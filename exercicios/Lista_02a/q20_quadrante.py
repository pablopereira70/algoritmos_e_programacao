"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    angulo = int(input('Digite um ângulo do intervalo 0° a 360°: '))
    
    if angulo >= 0 and angulo <= 360:
        eh_eixo = verificar_se_eh_eixo(angulo)
        if eh_eixo:
            print(f'O ângulo {angulo}° não pertence a nenhum quadrante')
        else:
            quadrante = obter_quadrante(angulo)
            print(f'O ângulo {angulo}° pertence ao {quadrante} quadrante')
    else:
        print('ÂNGULO INVÁLIDO')


def verificar_se_eh_eixo(Â):
    return Â == 0 or Â == 90 or Â == 180 or Â == 270 or Â == 360 


def obter_quadrante(Â):
    if Â > 0 and Â < 90:
        return 'primeiro'
    elif Â > 90 and Â < 180:
        return 'segundo'
    elif Â > 180 and Â < 270:
        return 'terceiro'
    else:
        return 'quarto'
    

main()