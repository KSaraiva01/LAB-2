
def main():
    try:
        nome = input("Digite o nome que quer verificar :")
        arquivo = open('nomes.txt', 'r')
        nomes = arquivo.readlines()
        for linha in nomes:
            if nome in linha:
                print("O nome", nome, "esta na lista")
                break
        arquivo.close()
    except ValueError:
        print("Valor invalido!!")

main()

