

def main():
    dicionario = {}
    while True:
        chave = input("Informe uma chave para seu dicionario:")
        valor = input("Informe uma valor para seu dicionario:")
        if not chave:
            break
        dicionario[chave] = valor
        print(dicionario)

main()

