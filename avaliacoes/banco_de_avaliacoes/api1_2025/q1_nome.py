def main():
    nome = input("Digite seu nome: ")
    if len(nome) % 2 == 0:
        for i in range(1, 4):
            num = len(nome)
            print(num + num * i, end=" - ")
        print("fim")
    else:
        for i in range(len(nome), 0, -1):
            if len(nome) % i == 0:
                print(i, end= " - ")
        print("fim")


main()