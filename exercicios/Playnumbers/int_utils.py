def obter_inteiro(conteudo):
    while True:

        try:
            inteiro = int(input(conteudo))
            return inteiro
        except:
            print("Valor inválido. Isso não é um número inteiro(ex: ...,-2,-1,0,1,2,...)")


def obter_inteiro_positivo(conteudo):
    while True:

        try:
            inteiro = obter_inteiro(conteudo)

            if inteiro > 0:
                return inteiro
            
            erro = 1 / 0
        except:
            print("Valor inválido. Isso não é um número inteiro positivo(ex: 1,2,3,...)")


def obter_inteiro_minimo(conteudo, limite_inferior):
    while True:

        try:
            inteiro = obter_inteiro(conteudo)

            if inteiro >= limite_inferior:
                return inteiro
            
            erro = 1 / 0
        except:
            print(f"Valor inválido. Isso não é um número inteiro maior ou igual a {limite_inferior}.")


def obter_inteiro_maximo(conteudo, limite_superior):
    while True:

        try:
            inteiro = obter_inteiro(conteudo)

            if inteiro <= limite_superior:
                return inteiro
            
            erro = 1 / 0
        except:
            print(f"Valor inválido. Isso não é um número inteiro menor ou igual a {limite_superior}")


def obter_inteiro_intervalo(conteudo, limite_inferior, limite_superior):
    while True:
        try:
            inteiro = obter_inteiro(conteudo)

            if inteiro >= limite_inferior and inteiro <= limite_superior:
                return inteiro
            
            erro = 1 / 0
        except:
            print(f"Valor inválido. Isso não é um número inteiro do intervalo [{limite_inferior}, {limite_superior}]")