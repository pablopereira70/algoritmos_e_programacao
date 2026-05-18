from q2_int_utils import *
from q3_float_utils import *

def main():
    menu = '''
--- APP_EMPRÉSTIMO ---
[1] para iniciar
[0] para sair
----------------------'''
    
    while True:
        print(menu)
        comando = obter_inteiro_intervalo('-->', 0, 1)

        if comando == 1:
            renda_mensal = obter_inteiro_positivo('Digite sua renda mensal: ')
            valor_emprestimo = obter_real_minimo('Digite o  valor do empréstimo: ', 1518)
            prazo_desejado = obter_inteiro_minimo('Digite o número de parcelas: ', 2)

            valor_iof = obter_iof(valor_emprestimo, prazo_desejado)
            juros = obter_juros(valor_emprestimo + valor_iof, prazo_desejado)
            valor_total = valor_emprestimo + juros + valor_iof
            parcela = valor_total / prazo_desejado

            if parcela > (0.3 * renda_mensal):
                status = 'Negado'
            else:
                status = 'Aprovado'
                     
            print(f'''
--------- SITUAÇÃO ---------
IOF(R$):            {valor_iof:.2f}
Juros(R$):          {juros:.2f}
Total a pagar(R$):  {valor_total:.2f}
Parcela mensal(R$): {parcela:.2f}
Empréstimo:         {status}
----------------------------''')
        else:
            break


def obter_iof(valor, prazo):
    return valor * 0.0038 + valor * 0.000082 * prazo * 30

def obter_juros(valor, prazo):
    if prazo > 18:
        return valor * (0.1475 + 0.1475 * 0.3)
    elif prazo > 11:
        return valor * 0.1475
    elif prazo > 7:
        return valor * (0.1475 * 0.75)
    else:
        return valor * (0.1475 * 0.5)


main()