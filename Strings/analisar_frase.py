from utils import *

def main():
    menu = '''
--- APP ANALISAR FRASE ---
[1] para iniciar
[0] para sair
--------------------------'''
    while True:
        print(menu)
        comando = obter_inteiro_intervalo('-->', 0, 1)
        if comando == 1:
            texto = obter_frase_min("Digite sua frase: ", 5)
            quant_char = qtd_caracteres(texto)
            quant_palavras = qtd_palavras(texto)
            print(f'''
--- QUANTIDADE ---
caracteres: {quant_char}
palavras:   {quant_palavras}
------------------''')
            escrever_separado(texto)
        else:
            break

def obter_frase_min(conteudo, min):
    while True:
        try:
            texto = obter_texto_minimo(conteudo, 1)
            count_palavra = 1
            for ch in texto:
                if ch == ' ':
                    count_palavra += 1
            if count_palavra >= min:
                return texto
            erro = 1 / 0
        except:
            print(f'Digite uma frase com no mínimo {min} palavras')


def qtd_caracteres(texto):
    count = 0
    for ch in texto:
        if ch != ' ':
            count += 1
    return count


def qtd_palavras(texto):
    count = 1
    for ch in texto:
        if ch == ' ':
            count += 1
    return count


def escrever_separado(frase):
    fragmento = ''
    for ch in frase:
        if ch == ' ':
            print(fragmento)
            fragmento = ''
            continue
        fragmento += ch
    print(fragmento)
    
    
main()