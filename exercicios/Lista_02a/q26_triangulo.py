"""
Disciplina: Algoritmos e Programação
Módulo: 03 - Estruturas Condicionais
Descrição: Programa que verifica se três lados formam um triângulo retângulo.
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
     Lado_A = int(input('Digite o lado A: '))
     Lado_B = int(input('Digite o lado B: '))
     Lado_C = int(input('Digite o lado C: '))

     hipotenusa, cateto1 , cateto2 = verificar_lados(Lado_A,Lado_B,Lado_C)
     
     print(f"""
hipotenusa = {hipotenusa}
cateto = {cateto1}
cateto = {cateto2}
""")
     

def verificar_lados(A,B,C):
     if A > B and A > C:
          return A,B,C
     elif B > A and B > C:
          return B,A,C
     elif C > A and C > B:
          return C,A,B
     else:
          return 'INVÁLIDO','INVÁLIDO','INVÁLIDO'
     

main()