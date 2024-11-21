import random

def main():
    N = int(input("Digite a quantidade de números aleatórios : "))
    arquivo = open("numeros.txt", "w")
    for i in range(N):
        numero = random.randint(0, 100)
        arquivo.write(f"{numero}\n") 

main()