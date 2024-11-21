def main():
    arquivo = open("artigo.txt", "r")
    texto = arquivo.read()
    palavras = texto.split()
    contador = {}
    for palavra in palavras:
        palavra = palavra.lower()
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1
    for palavra in contador:
        print("'",palavra,"' Apareceu", contador[palavra]," vezes")

main()