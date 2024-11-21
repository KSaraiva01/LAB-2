def main():
    try:
        arquivo = open("texto.txt", "r")
        texto = arquivo.read()
        palavras = texto.split()
        total = len(palavras)
        print("O número total de palavras no arquivo é:", total)
        arquivo.close
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado.")

main()