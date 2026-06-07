"""
Módulo: 04 - Estruturas de Repetição
Autor: Pablo Pereira
Data: Maio / 2026
"""

def main():
    n = int(input('Digite a quantidade de fichas: '))

    magro_id = None
    magro_kg = 999
    gordo_id = None
    gordo_kg = 0

    for i in range(n):
        num_id = input('Número de identificação: ')
        peso_kg = int(input('Peso (kg): '))

        if peso_kg > gordo_kg:
            gordo_id = num_id
            gordo_kg = peso_kg
            
        if peso_kg < magro_kg:
            magro_id = num_id
            magro_kg = peso_kg

    print('MAIS MAGRO')
    print(f'ID: {magro_id}')
    print(f'Peso: {magro_kg}')
    print('MAIS GORDO')
    print(f'ID: {gordo_id}')
    print(f'Peso: {gordo_kg}')


main()