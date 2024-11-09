
def main():
    arquivo = open("aula 30.10/teste.txt", "w")

    for i in range(50):
        arquivo.write(str(i))
        arquivo.write('\n')

    arquivo.close()

main()