from utils import *

def main():
    menu = '''
--- APP ANALISAR FRASE2 ---
[1] para iniciar
[0] para sair
---------------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo('-->', 0, 1)
        if comando == 1:
            frase = obter_texto_minimo_e_maximo('Digite a frase: ', 50, 180)
            quant_par = qtd_palavras_par(frase)
            quant_impar = qtd_palavras_impar(frase)
            maior_palavra = encontrar_maior_palavra(frase)
            menor_palavra = encontrar_menor_palavra(frase)
            print(f'''
--- ESTATISTÍCAS ---
palavras pares:   {quant_par}
palavras ímpares: {quant_impar}
maior palavra:    {maior_palavra}
menor palavra:    {menor_palavra}
--------------------''')
        else:
            break


def qtd_palavras_par(texto):
    count = 0
    fragmento = ''
    for ch in texto:
        if ch == ' ':
            if len(fragmento) % 2 == 0:
                count += 1
            fragmento = ''
            continue
        fragmento += ch
    return count


def qtd_palavras_impar(texto):
    count = 0
    fragmento = ''
    for ch in texto:
        if ch == ' ':
            if len(fragmento) % 2 != 0:
                count += 1
            fragmento = ''
            continue
        fragmento += ch
    return count


def encontrar_maior_palavra(texto):
    palavra = ''
    for ch in texto:
        if ch == ' ':
            break
        palavra += ch
    maior = palavra
    fragmento = ''
    for ch in texto:
        if ch == ' ':
            if len(fragmento) > len(maior):
                maior = fragmento
            fragmento = ''
            continue
        fragmento += ch
    if len(fragmento) > len(maior):
        maior = fragmento
    return maior



def encontrar_menor_palavra(texto):
    palavra = ''
    for ch in texto:
        if ch == ' ':
            break
        palavra += ch
    menor = palavra
    fragmento = ''
    for ch in texto:
        if ch == ' ':
            if len(fragmento) < len(menor):
                menor = fragmento
            fragmento = ''
            continue
        fragmento += ch
    if len(fragmento) < len(menor):
        menor = fragmento
    return menor


main()