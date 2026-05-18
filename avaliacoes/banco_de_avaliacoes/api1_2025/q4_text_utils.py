def obter_texto(conteudo):
    return input(conteudo)


def obter_texto_minimo_e_maximo(conteudo,min = 0, max = 999):
    while True:
        try:
            texto = input(conteudo)
            if len(texto) >= min and len(texto) <= max:
                return texto
            erro = 1 / 0
        except:
            print(f"Valor inválido. Isso não é um texto de {min} a {max} caracteres")