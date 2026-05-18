def obter_real(conteudo):
    while True:
        try:
            real = float(input(conteudo))
            return real
        except:
             print("Valor inválido. Isso não é um número real(ex: ...,-0.1,0.0,0.1,...)")


def obter_real_positivo(conteudo):
    while True:
        try:
            real = obter_real(conteudo)
            if real > 0:
                return real
            erro = 1 / 0
        except:
             print("Valor inválido. Isso não é um número real(ex: 0.1,0.2,0.3,...)")


def obter_real_minimo(conteudo, limite_inferior):
    while True:
        try:
            real = obter_real(conteudo)
            if real >= limite_inferior:
                return real
            erro = 1 / 0
        except:
             print(f"Valor inválido. Isso não é um número real maior ou igual a {limite_inferior}")


def obter_real_maximo(conteudo, limite_superior):
    while True:
        try:
            real = obter_real(conteudo)
            if real <= limite_superior:
                return real
            erro = 1 / 0
        except:
             print(f"Valor inválido. Isso não é um número real maior ou igual a {limite_superior}")


def obter_inteiro_intervalo(conteudo, limite_inferior, limite_superior):
    while True:
        try:
            inteiro = obter_real(conteudo)

            if inteiro >= limite_inferior and inteiro <= limite_superior:
                return inteiro
            
            erro = 1 / 0
        except:
            print(f"Valor inválido. Isso não é um número real do intervalo [{limite_inferior}, {limite_superior}]")