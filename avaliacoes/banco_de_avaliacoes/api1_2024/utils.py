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


def obter_real_intervalo(conteudo, limite_inferior, limite_superior):
    while True:
        try:
            real = obter_real(conteudo)

            if real >= limite_inferior and real <= limite_superior:
                return real
            
            erro = 1 / 0
        except:
            print(f"Valor inválido. Isso não é um número real do intervalo [{limite_inferior}, {limite_superior}]")


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

def obter_texto_minimo_e_maximo(conteudo,min = 0, max = 999):
    while True:
        try:
            texto = input(conteudo)
            if len(texto) >= min and len(texto) <= max:
                return texto
            erro = 1 / 0
        except:
            print(f"Valor inválido. Isso não é um texto de {min} a {max} caracteres")