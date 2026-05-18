"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que verifica a senha de acesso.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    senha_usuario = input('Digite a senha: ')
    
    senha = '1234'
    if senha_usuario == senha:
        print('Acesso concedido')
    else:
        print('Acesso negado')


main()