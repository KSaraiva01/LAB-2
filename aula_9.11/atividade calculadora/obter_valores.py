def obter_valores():
    while True:
        try:
            val1 = int(input("Digite o primeiro valor:")) 
            val2 = int(input("Digite o segundo valor:")) 
            return val1 , val2 
        except ValueError:
            print("Valor invalido")