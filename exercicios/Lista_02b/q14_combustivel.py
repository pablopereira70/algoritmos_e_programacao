"""
Módulo: 03 - Estruturas Condicionais
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    litro_vend = int(input('Digite a quantidade de litros abastecidos(L): '))
    tipo_comb = input('Digite o tipo de combustível abastecido(A/G): ')

    desc = calcular_desc(litro_vend, tipo_comb)
    valor_comb = calcular_valor_comb(litro_vend, tipo_comb)
    valor_client = valor_comb - desc

    print(f"Conta: R${valor_client:.2f}")
          

def calcular_desc(L, Comb):
    if Comb == "A":
        if L > 20:
            return (L * 1.9) * 0.05
        else:
            return (L * 1.9) * 0.03
    else:
        if L > 20:
            return (L * 2.5) * 0.06
        else:
            return (L * 2.5) * 0.04
        

def calcular_valor_comb(L, Comb):
    if Comb == "A":
        return L * 1.9
    else:
        return L * 2.5
    

main()