def main():
    try:
        arquivo1 = open('lista1.txt', 'r')
        lista1 = arquivo1.readlines()
        arquivo2 = open('lista2.txt', 'r')
        lista2 = arquivo2.readlines()
        diferenca = []
        for produto in lista1:
            if produto not in lista2:
                diferenca.append(produto)
        Resultado = open('diferenca.txt', 'a')
        for produto in diferenca:
            Resultado.write(produto + '\n') 
        arquivo1.close()
        arquivo2.close()
        Resultado.close()
    except :
        print("Erro: O arquivo não foi encontrado.")

main()